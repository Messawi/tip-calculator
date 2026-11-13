"""
tip_calculator.py  —  Lab 2 (ENGR403)

Build these three functions using Test-Driven Development.
Write a FAILING test first, then write just enough code here to pass.

Delete the `raise NotImplementedError` lines as you implement each one.
"""


def calculate_tip(bill, tip_pct):
    """Return the tip amount for a bill at the given tip percentage.

    Example: calculate_tip(100, 15) -> 15.0
    Raise ValueError if bill or tip_pct is negative.
    """
    return bill * tip_pct / 100


def calculate_total(bill, tip_pct):
    """Return bill + tip.

    Example: calculate_total(100, 15) -> 115.0
    """
    return bill + calculate_tip(bill, tip_pct)


def split_bill(total, people):
    """Return the per-person amount, rounded to 2 decimals.

    Example: split_bill(115, 2) -> 57.5
    Raise ValueError if people <= 0.
    """
    raise NotImplementedError
