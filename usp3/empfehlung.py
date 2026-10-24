"""Erster Prototyp des Empfehlungsalgorithmus (USP III).

Grundlagen:
- usp3/CLUSTERUNG.md
- usp3/BEWERTUNGSBOGEN.md
- ENTSCHEIDUNGSVORLAGE-USP3.md

Zwei Varianten, die gegeneinander getestet werden:
- "nachbar": Ähnlichkeit zu einzelnen gut bewerteten Büchern (einfache Vergleichsvariante)
- "cluster": mehrere Geschmacksgruppen je Person; jeder Kandidat zählt nur in seiner
  am besten passenden Gruppe

Alle Zahlen sind Entwurfswerte, nicht belegt. Die Tests prüfen die Logik, nicht ob die
empfohlenen Bücher tatsächlich gefallen.

    python3 usp3/empfehlung.py --self-test
    python3 usp3/empfehlung.py --demo
"""

from collections import defaultdict
import argparse
import unittest

# --- Entwurfswerte (zu testen, nicht belegt) --------------------------------------
LAMBDA = 3.0            # Dämpfung der Präferenz: Σ(w·y) / (λ + Σw)
STAR_TRANSFER = 0.3     # schwacher Übertrag der Gesamtbewertung auf vorhandene Merkmale
POS_THRESHOLD = 4       # Ankerbücher: 4–5 Lichter
MIN_COVERAGE = 0.6      # unter dieser Merkmalsabdeckung wird die Ähnlichkeit gedämpft
CLUSTER_LINK = 0.5      # Ähnlichkeit, ab der Ankerbücher dieselbe Gruppe bilden
PREF_WEIGHT = 0.3       # Einfluss gelernter Merkmalspräferenzen auf den Rang
AUTHOR_WEIGHT = 0.2
SELTENER_PENALTY = 0.3
DROP_AUTHOR_W = 0.3     # Abbruch ohne Urteil: schwacher, markierter Autorenübertrag
OWN_REC_W = 1.5         # Korrektur einer eigenen Empfehlungsannahme (Variante C)

DIMENSIONS = ('genre', 'thema', 'tempo', 'ton', 'fokus', 'sprache', 'laenge', 'inhalt')
# Aspekt im Bogen (F3) → Merkmalsdimension des Buchs
ASPECT_DIM = {'Sprache': 'sprache', 'Figuren': 'fokus', 'Handlung': 'tempo',
              'Atmosphäre': 'ton', 'Thema': 'thema'}
# Abbruchgrund (F4) → Dimension; None = kein Geschmackssignal auf ein Merkmal
DROP_REASON_DIM = {'Stil/Sprache': 'sprache', 'Tempo': 'tempo', 'Thema': 'thema',
                   'Figuren': 'fokus', 'Zu lang': 'laenge', 'Zu schwer': None,
                   'Nicht mein Genre': 'genre', 'Inhaltlich unangenehm': None,
                   'Erwartung nicht erfüllt': None, 'Anderes': None}


def feats(work, dim):
    """Bekannte Werte einer Dimension als Menge; leer = unbekannt (nicht: 'nicht vorhanden')."""
    v = work.get('features', {}).get(dim)
    if v is None:
        return set()
    return set(v) if isinstance(v, (list, tuple, set)) else {v}


def damped(evidence):
    """Gedämpfte Präferenz, liegt immer in [-1, 1]. evidence: Liste (w, y)."""
    sw = sum(w for w, _ in evidence)
    return sum(w * y for w, y in evidence) / (LAMBDA + sw) if evidence else 0.0


class Profile:
    """Aus den aktuellen Urteilen einer Person abgeleitet; ein Urteil je Werk."""

    def __init__(self, catalog, judgments, rec_feedback=()):
        self.catalog = catalog
        self.judgments = {}                       # work_id -> letztes Urteil
        for j in judgments:                       # spätere Bearbeitung ersetzt frühere
            self.judgments[j['work_id']] = j
        self.anchors = []                         # (work_id, Gewicht)
        self.pref = defaultdict(list)             # (kontext, dim, wert) -> [(w, y)]
        self.author = defaultdict(list)           # autor -> [(w, y)]
        self.never, self.seltener = set(), set()  # {(dim, wert)}
        self.blocked_titles = set()
        self.touched = set()                      # gelesen/begonnen/abgebrochen
        self._build()
        for fb in rec_feedback:
            self._own_recommendation_feedback(fb)

    def _build(self):
        for wid, j in self.judgments.items():
            work = self.catalog[wid]
            status = j.get('status')
            if status in ('read', 'drop', 'reading'):
                self.touched.add(wid)
            if status == 'paused' and j.get('stars') is None:
                continue                              # Pause ohne Urteil: geschmacksneutral
            stars = j.get('stars')
            context = next(iter(sorted(feats(work, 'genre'))), None)
            if stars is not None and stars >= POS_THRESHOLD:
                self.anchors.append((wid, (stars - 3) / 2))
            if stars is not None:                      # schwacher Übertrag, kontextgebunden
                y = (stars - 3) / 2
                if y:
                    for dim in DIMENSIONS:
                        if dim in ('genre', 'inhalt', 'laenge'):
                            continue
                        for v in feats(work, dim):
                            self.pref[(context, dim, v)].append((STAR_TRANSFER, y))
            for aspect, val in (j.get('aspects') or {}).items():
                dim = ASPECT_DIM.get(aspect)
                if dim is None or val not in (1, -1):  # 'gemischt' und leer: keine Richtung
                    continue
                for v in feats(work, dim):             # ohne Buchmerkmal: keine erfundene Vorliebe
                    self.pref[(context, dim, v)].append((1.0, float(val)))
            if j.get('tempo') in ('zu_langsam', 'zu_schnell'):
                for v in feats(work, 'tempo'):
                    self.pref[(context, 'tempo', v)].append((1.0, -1.0))
            if status == 'drop':
                self.blocked_titles.add(wid)
                for reason in j.get('reasons', []):
                    dim = DROP_REASON_DIM.get(reason)
                    if dim:
                        for v in feats(work, dim):
                            self.pref[(context, dim, v)].append((1.0, -1.0))
            more = j.get('more_author')              # F2: ja / nein / unsicher / None
            for a in feats(work, 'autor'):
                if more == 'ja':
                    self.author[a].append((1.0, 1.0))
                elif more == 'nein':
                    self.author[a].append((1.0, -1.0))
                elif status == 'drop' and (stars is None or stars <= 2) and more is None:
                    self.author[a].append((DROP_AUTHOR_W, -1.0))
            for ex in j.get('exclusions', []):
                target = self.never if ex['action'] == 'never' else self.seltener
                target.add((ex['dimension'], ex['value_id']))

    def _own_recommendation_feedback(self, fb):
        """Variante C: Die Annahme, mit der die App empfohlen hat, wird gezielt korrigiert."""
        if fb.get('fit') not in ('nein', 'teilweise'):
            return
        for dim, val in fb.get('assumptions', {}).items():
            if dim in fb.get('failed_dims', ()):
                self.pref[(None, dim, val)].append((OWN_REC_W, -1.0))

    def pref_for(self, cand, dim, v):
        cg = feats(cand, 'genre')
        ev = list(self.pref.get((None, dim, v), []))
        for g in cg:
            ev += self.pref.get((g, dim, v), [])
        return damped(ev)


def similarity(cand, anchor, judgment=None):
    """Ähnlichkeit über gemeinsam bekannte Merkmale. Gibt (sim, abdeckung, treffer) zurück.
    Fehlende Angaben zählen weder als Übereinstimmung noch als Widerspruch."""
    liked = {ASPECT_DIM[a] for a, v in ((judgment or {}).get('aspects') or {}).items()
             if v == 1 and a in ASPECT_DIM}
    num = den = 0.0
    known_anchor = [d for d in DIMENSIONS if feats(anchor, d) and d != 'inhalt']
    shared, hits = 0, []
    for d in known_anchor:
        a, c = feats(anchor, d), feats(cand, d)
        if not c:
            continue
        shared += 1
        w = 2.0 if d in liked else 1.0
        m = len(a & c) / len(a | c)
        num += w * m
        den += w
        if m > 0:
            hits.append((d, sorted(a & c)))
    if not den:
        return 0.0, 0.0, []
    cov = shared / len(known_anchor)
    return (num / den) * min(1.0, cov / MIN_COVERAGE), cov, hits


def clusters(profile):
    """Ankerbücher einer Person gruppieren (einfache Verknüpfung); überlappungsfrei."""
    ids = [w for w, _ in profile.anchors]
    group = {w: {w} for w in ids}
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            s, _, _ = similarity(profile.catalog[b], profile.catalog[a])
            if s >= CLUSTER_LINK and group[a] is not group[b]:
                merged = group[a] | group[b]
                for w in merged:
                    group[w] = merged
    out = []
    for g in group.values():
        if g not in out:
            out.append(g)
    return out


def recommend(catalog, profile, variant='cluster', k=5):
    weights = dict(profile.anchors)
    groups = clusters(profile) if variant == 'cluster' else [{w} for w in weights]
    seen_titles, results = set(), []
    for wid, cand in catalog.items():
        title_key = cand.get('work_key', wid)          # zwei ISBN = ein Werk
        if wid in profile.touched or title_key in seen_titles or wid in profile.blocked_titles:
            continue
        if any(title_key == catalog[t].get('work_key', t) for t in profile.touched):
            continue
        blocked, unknown = False, []
        for dim, val in profile.never:                 # harter Ausschluss
            if not cand.get('checked', {}).get(dim) and not feats(cand, dim):
                unknown.append(dim)                    # unbekannt ≠ enthält das nicht
            elif val in feats(cand, dim):
                blocked = True
        if blocked or unknown:
            continue
        best, best_info = 0.0, None
        for g in groups:
            sims = [(similarity(cand, catalog[a], profile.judgments.get(a)), a) for a in g]
            if not sims:
                continue
            score = sum(s[0] * weights[a] for s, a in sims) / len(sims)   # innerhalb der Gruppe
            if score > best:
                top = max(sims, key=lambda x: x[0][0])
                best, best_info = score, (sorted(g), top)
        if best_info is None:
            continue
        adj = 0.0
        known = [(d, v) for d in DIMENSIONS for v in feats(cand, d)]
        if known:
            adj += PREF_WEIGHT * sum(profile.pref_for(cand, d, v) for d, v in known) / len(known)
        for a in feats(cand, 'autor'):
            adj += AUTHOR_WEIGHT * damped(profile.author.get(a, []))
        for d, v in known:
            if (d, v) in profile.seltener:
                adj -= SELTENER_PENALTY
        (s, cov, hits), anchor = best_info[1]
        seen_titles.add(title_key)
        results.append({'work_id': wid, 'title': cand['title'], 'score': round(best + adj, 3),
                        'coverage': round(cov, 2), 'anchor': catalog[anchor]['title'],
                        'group': [catalog[w]['title'] for w in best_info[0]],
                        'reasons': hits if cov >= MIN_COVERAGE else [],
                        'low_coverage': cov < MIN_COVERAGE})
    results.sort(key=lambda r: -r['score'])
    return results[:k]


# --- Synthetischer Beispielkatalog (erfundene Titel, nur für Logiktests) -------------
def book(title, **f):
    key = f.pop('work_key', None)
    checked = f.pop('checked', {})
    d = {'title': title, 'features': f, 'checked': checked}
    if key:
        d['work_key'] = key
    return d


def demo_catalog():
    F = dict
    return {
        'fam1': book('Das Haus am Fluss', genre='Roman', thema=['Familie', 'Herkunft'], tempo='ruhig', ton='melancholisch', fokus='figuren', sprache='poetisch', laenge='mittel', autor='A. Lind', inhalt=[], checked=F(inhalt=True)),
        'fam2': book('Sommer der Schwestern', genre='Roman', thema=['Familie'], tempo='ruhig', ton='warm', fokus='figuren', sprache='poetisch', laenge='mittel', autor='B. Roth', inhalt=[], checked=F(inhalt=True)),
        'fam3': book('Die Küstenkinder', genre='Roman', thema=['Familie', 'Meer'], tempo='ruhig', ton='melancholisch', fokus='figuren', sprache='poetisch', laenge='lang', autor='C. Feld', inhalt=[], checked=F(inhalt=True)),
        'thr1': book('Nachtschicht', genre='Krimi & Thriller', thema=['Ermittlung'], tempo='rasant', ton='düster', fokus='handlung', sprache='nüchtern', laenge='mittel', autor='D. Kramer', inhalt=['gewalt'], checked=F(inhalt=True)),
        'thr2': book('Der zweite Schuss', genre='Krimi & Thriller', thema=['Ermittlung', 'Stadt'], tempo='rasant', ton='düster', fokus='handlung', sprache='nüchtern', laenge='mittel', autor='E. Vogt', inhalt=['gewalt'], checked=F(inhalt=True)),
        'thr3': book('Kaltes Wasser', genre='Krimi & Thriller', thema=['Ermittlung', 'Meer'], tempo='rasant', ton='düster', fokus='handlung', sprache='nüchtern', laenge='kurz', autor='F. Brandt', inhalt=[], checked=F(inhalt=True)),
        'mix1': book('Mittelweg', genre='Unterhaltung', thema=['Alltag'], tempo='ausgewogen', ton='heiter', fokus='beides', sprache='schlicht', laenge='mittel', autor='G. Neu', inhalt=[], checked=F(inhalt=True)),
        'fam4': book('Winter in Husum', genre='Roman', thema=['Familie', 'Schuld'], tempo='ruhig', ton='melancholisch', fokus='figuren', sprache='poetisch', laenge='mittel', autor='H. Sander', inhalt=[], checked=F(inhalt=True)),
        'thr4': book('Spur im Schnee', genre='Krimi & Thriller', thema=['Ermittlung'], tempo='rasant', ton='düster', fokus='handlung', sprache='nüchtern', laenge='mittel', autor='I. Wolf', inhalt=[], checked=F(inhalt=True)),
        'thr5': book('Der lange Atem', genre='Krimi & Thriller', thema=['Ermittlung'], tempo='ruhig', ton='düster', fokus='handlung', sprache='nüchtern', laenge='lang', autor='J. Ost', inhalt=[], checked=F(inhalt=True)),
        'unk1': book('Nur ein Genre bekannt', genre='Roman'),
        'thr6': book('Ohne Inhaltsangabe', genre='Krimi & Thriller', thema=['Ermittlung'], tempo='rasant', ton='düster', fokus='handlung', sprache='nüchtern', laenge='mittel', autor='K. Hahn'),
    }


def J(work_id, stars=None, status='read', **kw):
    return dict(work_id=work_id, stars=stars, status=status, **kw)


class Abnahmefaelle(unittest.TestCase):
    """Die 12 Fälle aus CLUSTERUNG.md, Abschnitt 7 (Logik, nicht Gefallen)."""

    def setUp(self):
        self.cat = demo_catalog()

    def ids(self, res):
        return [r['work_id'] for r in res]

    def test_01_zwei_lesewelten_bleiben_repraesentiert(self):
        p = Profile(self.cat, [J('fam1', 5), J('fam2', 5), J('thr1', 5), J('thr2', 5)])
        top = self.ids(recommend(self.cat, p, 'cluster', k=3))
        self.assertTrue({'fam3', 'fam4'} & set(top[:3]))
        self.assertTrue({'thr3', 'thr4'} & set(top[:3]))
        self.assertNotEqual(top[0], 'mix1')
        self.assertNotIn('mix1', top[:3])

    def test_02_langsamer_thriller_lehnt_ruhige_romane_nicht_ab(self):
        base = Profile(self.cat, [J('fam1', 5)])
        crit = Profile(self.cat, [J('fam1', 5), J('thr5', 1, tempo='zu_langsam', aspects={'Handlung': -1})])
        s0 = {r['work_id']: r['score'] for r in recommend(self.cat, base, k=20)}['fam4']
        s1 = {r['work_id']: r['score'] for r in recommend(self.cat, crit, k=20)}['fam4']
        self.assertGreaterEqual(s1, s0)

    def test_03_duester_ist_kein_minus(self):
        p = Profile(self.cat, [J('thr1', 5)])
        for (ctx, dim, v), ev in p.pref.items():
            if dim == 'ton' and v == 'düster':
                self.assertGreater(damped(ev), 0)

    def test_04_ausschluss_gewinnt_gegen_hohe_passung(self):
        p = Profile(self.cat, [J('thr1', 5, exclusions=[dict(action='never', dimension='inhalt', value_id='gewalt')])])
        self.assertNotIn('thr2', self.ids(recommend(self.cat, p, k=20)))

    def test_05_fehlende_angabe_gilt_nicht_als_gewaltfrei(self):
        p = Profile(self.cat, [J('thr1', 5, exclusions=[dict(action='never', dimension='inhalt', value_id='gewalt')])])
        self.assertNotIn('thr6', self.ids(recommend(self.cat, p, k=20)))
        self.assertIn('thr4', self.ids(recommend(self.cat, p, k=20)))

    def test_06_abbruch_5_keine_zeit_bleibt_positiv_ohne_autorenmalus(self):
        p = Profile(self.cat, [J('fam1', 5, status='drop', reasons=['Anderes'])])
        self.assertIn('fam1', [w for w, _ in p.anchors])
        self.assertEqual(damped(p.author.get('A. Lind', [])), 0.0)

    def test_07_pause_ohne_urteil_aendert_nichts(self):
        a = Profile(self.cat, [J('fam1', 5)])
        b = Profile(self.cat, [J('fam1', 5), J('thr1', None, status='paused')])
        self.assertEqual(dict(a.pref), dict(b.pref))
        self.assertEqual(a.anchors, b.anchors)

    def test_08_figuren_gefielen_ohne_figurenmerkmal_keine_vorliebe(self):
        p = Profile(self.cat, [J('unk1', 5, aspects={'Figuren': 1})])
        self.assertFalse([k for k in p.pref if k[1] == 'fokus'])

    def test_09_kandidat_mit_einem_merkmal_geringe_abdeckung(self):
        p = Profile(self.cat, [J('fam1', 5)])
        r = {x['work_id']: x for x in recommend(self.cat, p, k=20)}
        self.assertTrue(r['unk1']['low_coverage'])
        self.assertEqual(r['unk1']['reasons'], [])
        self.assertLess(r['unk1']['score'], r['fam4']['score'])

    def test_10_geaenderte_bewertung_ersetzt_alte(self):
        p = Profile(self.cat, [J('fam1', 2), J('fam1', 5)])
        self.assertEqual(len(p.judgments), 1)
        self.assertIn('fam1', [w for w, _ in p.anchors])

    def test_11_gleicher_titel_zwei_isbn(self):
        cat = dict(self.cat)
        cat['fam4b'] = dict(self.cat['fam4'], work_key='fam4')
        cat['fam4'] = dict(self.cat['fam4'], work_key='fam4')
        p = Profile(cat, [J('fam1', 5)])
        ids = self.ids(recommend(cat, p, k=20))
        self.assertEqual(len([i for i in ids if i.startswith('fam4')]), 1)

    def test_12_eigenempfehlung_scheitert_an_tempo(self):
        fb = dict(fit='nein', assumptions={'tempo': 'ruhig', 'thema': 'Familie'}, failed_dims={'tempo'})
        p = Profile(self.cat, [J('fam1', 5)], rec_feedback=[fb])
        q = Profile(self.cat, [J('fam1', 5)])
        self.assertLess(p.pref_for(self.cat['fam4'], 'tempo', 'ruhig'), q.pref_for(self.cat['fam4'], 'tempo', 'ruhig'))
        self.assertEqual(p.pref_for(self.cat['fam4'], 'thema', 'Familie'), q.pref_for(self.cat['fam4'], 'thema', 'Familie'))
        self.assertEqual(dict(p.author), dict(q.author))

    def test_13_damped_bleibt_im_wertebereich(self):
        self.assertLessEqual(abs(damped([(2.0, 1.0)] * 50)), 1.0)
        self.assertAlmostEqual(damped([(1.0, -1.0)] * 5), -5 / 8)


def demo():
    cat = demo_catalog()
    judg = [J('fam1', 5, aspects={'Sprache': 1, 'Figuren': 1}, more_author='ja'),
            J('fam2', 4, aspects={'Atmosphäre': 1}),
            J('thr1', 5, aspects={'Handlung': 1}),
            J('thr2', 4, exclusions=[dict(action='seltener', dimension='thema', value_id='Stadt')]),
            J('thr5', 2, status='drop', reasons=['Tempo'], tempo='zu_langsam')]
    p = Profile(cat, judg)
    print('SYNTHETISCHER KATALOG – prüft Logik, nicht Gefallen\n')
    print('Geschmacksgruppen (cluster):', [[cat[w]['title'] for w in g] for g in clusters(p)])
    for variant in ('nachbar', 'cluster'):
        print(f'\nVariante {variant}:')
        for r in recommend(cat, p, variant):
            why = ', '.join(f"{d}: {'/'.join(v)}" for d, v in r['reasons'][:3]) or 'zu wenig bekannte Merkmale'
            print(f"  {r['score']:+.3f}  {r['title']:<24} Anker: {r['anchor']:<22} Abdeckung {r['coverage']:.0%}  ({why})")


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--demo', action='store_true')
    a = ap.parse_args()
    if a.self_test:
        unittest.main(argv=['empfehlung.py', '-v'])
    else:
        demo()
