"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitPatentGuard.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.prior_art_similarity_scorer import *
from tools.claim_breadth_analyzer import *
from tools.patent_expiration_calculator import *

class TestGitPatentGuardPredictability(unittest.TestCase):

    def test_prior_art_similarity_scorer(self):
        res = score_prior_art('{"claim_text": "A widget comprising solar cells", "prior_art_text": "An apparatus comprising hydraulic valves"}')
        self.assertFalse(res["high_overlap_flag"])
        self.assertEqual(res["status"], "NOVELTY_CLEARED")

    def test_claim_breadth_analyzer(self):
        res = analyze_claim_breadth("A system comprising: a processor; a memory coupled to the processor; and a wireless transceiver configured to transmit telemetry.")
        self.assertTrue(res["sufficient_limitations"])
        self.assertEqual(res["status"], "CLAIM_SCOPE_VALID")

    def test_patent_expiration_calculator(self):
        res = calculate_patent_expiration(2015)
        self.assertEqual(res["expiration_year"], 2035)
        self.assertTrue(res["active"])


if __name__ == "__main__":
    unittest.main()
