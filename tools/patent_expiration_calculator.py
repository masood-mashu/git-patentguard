"""
patent_expiration_calculator.py - Calculates 20-year statutory patent expiration date from initial non-provisional filing date
"""
import sys
import json


def calculate_patent_expiration(filing_year: int):
    expiry = filing_year + 20
    is_active = 2026 < expiry
    return {
        "filing_year": filing_year,
        "expiration_year": expiry,
        "active": is_active,
        "status": "PATENT_ACTIVE" if is_active else "PATENT_EXPIRED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "patent-expiration-calculator"}))
