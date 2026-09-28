"""
prior_art_similarity_scorer.py - Scores textual similarity between proposed invention claims and cited prior art references
"""
import sys
import json


def score_prior_art(claim_comparison_json: str):
    import json
    data = json.loads(claim_comparison_json) if isinstance(claim_comparison_json, str) else claim_comparison_json
    c_words = set(data.get("claim_text", "").lower().split())
    p_words = set(data.get("prior_art_text", "").lower().split())
    
    if not c_words or not p_words:
        sim = 0.0
    else:
        sim = len(c_words.intersection(p_words)) / max(len(c_words.union(p_words)), 1) * 100.0
    high_overlap = sim > 80.0
    return {
        "similarity_score": round(sim, 2),
        "high_overlap_flag": high_overlap,
        "status": "PRIOR_ART_CONFLICT" if high_overlap else "NOVELTY_CLEARED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "prior-art-similarity-scorer"}))
