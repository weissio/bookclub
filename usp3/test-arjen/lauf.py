"""Erster Testlauf mit Arjens Büchern: drei Varianten, verblindete Vorlage.

    python3 usp3/test-arjen/lauf.py

Schreibt:
- usp3/test-arjen/vorlage-verblindet.md  (für Arjen: Empfehlungen ohne Variantennamen)
- usp3/test-arjen/schluessel.json        (welche Empfehlung aus welcher Variante; erst nach dem Urteil öffnen)
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from empfehlung import Profile, recommend  # noqa: E402

KAT = os.path.join(os.path.dirname(HERE), 'katalog')
ASPEKTE = {'sprache': 'Sprache', 'figuren': 'Figuren', 'handlung': 'Handlung',
           'atmosphaere': 'Atmosphäre', 'thema': 'Thema'}
WERT = {'gefiel mir': 1, 'gemischt': 'gemischt', 'gefiel mir nicht': -1}


def to_work(e):
    f = {k: e.get(k) for k in ('genre', 'thema', 'tempo', 'ton', 'fokus', 'sprache', 'laenge')}
    f['autor'] = e.get('autor')
    f = {k: v for k, v in f.items() if v not in (None, [], '')}
    checked = {}
    if e.get('inhalt') is not None:
        f['inhalt'] = e['inhalt']
        checked['inhalt'] = True
    return {'title': e['titel'], 'autor_anzeige': e.get('autor'), 'features': f, 'checked': checked,
            'welt': e.get('welt')}


def load():
    cat = {}
    for e in json.load(open(os.path.join(KAT, 'kandidaten.json'), encoding='utf-8')):
        cat[e['id']] = to_work(e)
    mine = json.load(open(os.path.join(KAT, 'arjen-buecher.json'), encoding='utf-8'))
    for e in mine:
        cat[e['id']] = to_work(e)
    rows = list(csv.DictReader(open(os.path.join(HERE, 'meine-buecher.csv'), encoding='utf-8'), delimiter=';'))
    judg = []
    for e, r in zip(mine, rows):
        aspects = {}
        for col, name in ASPEKTE.items():
            v = WERT.get((r.get(col) or '').strip().lower())
            if v is not None:
                aspects[name] = v
        status = {'gelesen': 'read', 'abgebrochen': 'drop'}.get(r['status'].strip().lower(), 'read')
        more = {'ja': 'ja', 'nein': 'nein', 'weiß nicht': 'unsicher'}.get((r.get('mehr_von_person') or '').strip().lower())
        tempo = {'zu langsam': 'zu_langsam', 'zu_langsam': 'zu_langsam', 'passend': 'passend',
                 'zu schnell': 'zu_schnell', 'zu_schnell': 'zu_schnell'}.get((r.get('tempo_fuer_mich') or '').strip().lower())
        judg.append(dict(work_id=e['id'], stars=int(float(r['lichter'])) if r['lichter'] else None,
                         status=status, aspects=aspects, more_author=more, tempo=tempo,
                         reasons=[x.strip() for x in (r.get('abbruchgruende') or '').split(',') if x.strip()]))
    return cat, judg


def main():
    cat, judg = load()
    arms = {
        'nachbar': recommend(cat, Profile(cat, judg), 'nachbar', k=5),
        'cluster': recommend(cat, Profile(cat, judg), 'cluster', k=5),
        'nur_f1': recommend(cat, Profile(cat, judg, use_aspects=False), 'nachbar', k=5),
    }
    pool = {}
    for arm, res in arms.items():
        for rank, r in enumerate(res, 1):
            p = pool.setdefault(r['work_id'], {'r': r, 'arme': {}})
            p['arme'][arm] = rank
    items = list(pool.values())
    random.Random(20261024).shuffle(items)
    lines = ['# Empfehlungen zur Beurteilung (verblindet)', '',
             'Bitte je Buch: **Würde ich lesen?** Ja / Vielleicht / Nein · **Passt die Begründung?** Ja / Teilweise / Nein · optional ein Satz.',
             'Kennst du ein Buch schon, schreib „kenne ich“ und wie es dir gefallen hat.', '']
    key = {}
    for i, p in enumerate(items, 1):
        r = p['r']; w = cat[r['work_id']]
        why = '; '.join(f"{d}: {', '.join(v)}" for d, v in r['reasons']) or 'nur wenige Merkmale bekannt'
        lines += [f"**{i}. {w['title']}** – {w['autor_anzeige']}",
                  f"Ähnlich zu: {r['anchor']} · Gemeinsam: {why} · Datenabdeckung {r['coverage']:.0%}", '']
        key[i] = {'work_id': r['work_id'], 'titel': w['title'], 'arme_rang': p['arme'], 'score': r['score']}
    open(os.path.join(HERE, 'vorlage-verblindet.md'), 'w', encoding='utf-8').write('\n'.join(lines))
    json.dump(key, open(os.path.join(HERE, 'schluessel.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('\n'.join(lines))
    print(f"\n{len(items)} verschiedene Empfehlungen aus 3 Varianten.")


if __name__ == '__main__':
    main()
