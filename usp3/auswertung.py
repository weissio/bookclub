"""Auswertung echter Empfehlungsverläufe, keine Empfehlungsmaschine.

python3 auswertung.py --self-test
python3 auswertung.py verlaeufe.json --as-of 2027-01-01 --window-days 60

JSON: Liste mit genau einem Verlauf pro Person und Werk (nicht pro Anzeige).
Pflichtfelder: user_id, work_id, arm, served_at (ISO-Datum).
Optional: started_at, attributed (bool), feedback_at, stars (1..5),
status (read/drop/reading/paused), exclusion_violation (bool oder null).
feedback_at bezeichnet das Datum der aktuellen Bewertung. Historische Auswertung
braucht einen damaligen Datenexport; spätere Bearbeitungen nicht zurückdatieren.
"""

import argparse
from collections import defaultdict
from datetime import date
import json
import unittest


def ratio(n, d):
    return n / d if d else None


def evaluate(rows, as_of, window_days=60):
    cutoff = date.fromisoformat(as_of)
    if window_days < 0:
        raise ValueError('window_days muss >= 0 sein')
    seen = set()
    arms = defaultdict(list)
    for row in rows:
        key = (row['user_id'], row['work_id'])
        if key in seen:
            raise ValueError('Doppelter Verlauf für Person/Werk; Anzeigen zusammenführen')
        seen.add(key)
        served = date.fromisoformat(row['served_at'])
        started = date.fromisoformat(row['started_at']) if row.get('started_at') else None
        feedback = date.fromisoformat(row['feedback_at']) if row.get('feedback_at') else None
        stars = row.get('stars')
        if stars is not None and (type(stars) is not int or stars not in range(1, 6)):
            raise ValueError('Fehlende Lichter als null, sonst ganzzahlig 1..5')
        if stars is not None and feedback is None:
            raise ValueError('Bewertung braucht feedback_at')
        if started and started < served:
            raise ValueError('Beginn liegt vor Empfehlung')
        if feedback and (not started or feedback < started):
            raise ValueError('Feedback liegt vor Beginn oder Beginn fehlt')
        if row.get('attributed') not in (True, False, None):
            raise ValueError('attributed muss bool oder null sein')
        if row.get('exclusion_violation') not in (True, False, None):
            raise ValueError('exclusion_violation muss bool oder null sein')
        if stars is not None and row.get('status') not in ('read', 'drop'):
            raise ValueError('Diese Auswertung misst Gefallen nach Lesen oder Abbruch')
        if served <= cutoff and (cutoff - served).days >= window_days:
            arms[row['arm']].append((row, started, feedback))

    report = {}
    for arm, sample in sorted(arms.items()):
        begun, rated = [], []
        for row, started, feedback in sample:
            if started and started <= cutoff and row.get('attributed') is True:
                begun.append(row)
                if feedback and feedback <= cutoff and row.get('stars') is not None:
                    rated.append(row)
        positives = sum(r['stars'] >= 4 for r in rated)
        negatives = sum(r['stars'] <= 2 for r in rated)
        per_user = defaultdict(list)
        for row in rated:
            per_user[row['user_id']].append(row['stars'] >= 4)
        user_rates = [sum(values) / len(values) for values in per_user.values()]
        checked = [r for r, _, _ in sample if r.get('exclusion_violation') is not None]
        violations = sum(r['exclusion_violation'] is True for r in checked)
        report[arm] = {
            'mature_served_works': len(sample),
            'attributed_started_works': len(begun),
            'rated_works': len(rated),
            'positive_works_4_5': positives,
            'negative_works_1_2': negatives,
            'neutral_works_3': len(rated) - positives - negatives,
            'positive_share_among_rated': ratio(positives, len(rated)),
            'positive_share_user_macro': ratio(sum(user_rates), len(user_rates)),
            'rating_coverage_among_attributed_starts': ratio(len(rated), len(begun)),
            'attributed_starts_without_rating': len(begun) - len(rated),
            'rated_abandoned_works': sum(r.get('status') == 'drop' for r in rated),
            'positive_abandoned_works': sum(r.get('status') == 'drop' and r['stars'] >= 4 for r in rated),
            'exclusions_checked_works': len(checked),
            'exclusion_violations': violations,
            'exclusion_check_unknown_works': len(sample) - len(checked),
            'rated_users': len(per_user),
        }
    return {'as_of': as_of, 'window_days': window_days, 'arms': report}


class EvaluationTests(unittest.TestCase):
    def row(self, **patch):
        base = dict(user_id='u1', work_id='w1', arm='cluster', served_at='2026-01-01',
                    started_at='2026-01-02', attributed=True, feedback_at='2026-01-20',
                    stars=5, status='read', exclusion_violation=False)
        return dict(base, **patch)

    def result(self, rows):
        return evaluate(rows, '2026-04-01')['arms']['cluster']

    def test_positive_abandonment_is_positive(self):
        r = self.result([self.row(status='drop')])
        self.assertEqual(r['positive_share_among_rated'], 1)
        self.assertEqual(r['positive_abandoned_works'], 1)

    def test_missing_is_not_negative_or_neutral(self):
        r = self.result([self.row(stars=None, feedback_at=None, status='reading')])
        self.assertIsNone(r['positive_share_among_rated'])
        self.assertEqual(r['negative_works_1_2'], 0)
        self.assertEqual(r['neutral_works_3'], 0)
        self.assertEqual(r['attributed_starts_without_rating'], 1)

    def test_neutral_is_observed(self):
        self.assertEqual(self.result([self.row(stars=3)])['neutral_works_3'], 1)

    def test_unconfirmed_origin_is_not_attributed(self):
        r = self.result([self.row(attributed=False)])
        self.assertEqual(r['rated_works'], 0)
        self.assertEqual(r['mature_served_works'], 1)

    def test_duplicate_exposures_cannot_inflate_result(self):
        with self.assertRaises(ValueError):
            self.result([self.row(), self.row()])

    def test_future_feedback_not_used(self):
        r = self.result([self.row(feedback_at='2026-05-01')])
        self.assertEqual(r['rated_works'], 0)

    def test_immature_recommendations_not_used(self):
        rows = [self.row(served_at='2026-03-01', started_at='2026-03-02', feedback_at='2026-03-20')]
        self.assertEqual(evaluate(rows, '2026-04-01')['arms'], {})

    def test_unknown_exclusion_not_claimed_safe(self):
        r = self.result([self.row(exclusion_violation=None)])
        self.assertEqual(r['exclusions_checked_works'], 0)
        self.assertEqual(r['exclusion_check_unknown_works'], 1)

    def test_positive_rating_does_not_erase_exclusion_violation(self):
        r = self.result([self.row(exclusion_violation=True)])
        self.assertEqual(r['exclusion_violations'], 1)
        self.assertEqual(r['positive_works_4_5'], 1)

    def test_macro_does_not_overweight_prolific_rater(self):
        rows = [self.row(), self.row(work_id='w2'), self.row(user_id='u2', work_id='w3', stars=1)]
        r = self.result(rows)
        self.assertAlmostEqual(r['positive_share_among_rated'], 2 / 3)
        self.assertEqual(r['positive_share_user_macro'], .5)

    def test_zero_is_not_a_rating(self):
        with self.assertRaises(ValueError):
            self.result([self.row(stars=0)])

    def test_rating_coverage_exposes_missing_outcomes(self):
        rows = [self.row(), self.row(work_id='w2', stars=None, feedback_at=None, status='paused')]
        r = self.result(rows)
        self.assertEqual(r['positive_share_among_rated'], 1)
        self.assertEqual(r['rating_coverage_among_attributed_starts'], .5)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?')
    parser.add_argument('--as-of')
    parser.add_argument('--window-days', type=int, default=60)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        unittest.main(argv=['auswertung.py'])
    else:
        if not args.input or not args.as_of:
            parser.error('Eingabedatei und --as-of erforderlich')
        with open(args.input, encoding='utf-8') as handle:
            result = evaluate(json.load(handle), args.as_of, args.window_days)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
