"""
Your test suite for Lab 2. One sample test is provided to get you started.

Requirements (see the Lab 2 assignment):
  - at least 8 test functions total
  - at least one fixture
  - at least one @pytest.mark.parametrize
  - at least 2 error/edge-case tests (e.g., negative bill, zero people)
  - >= 80% branch coverage

Practice TDD on at least 2 of the three functions:
  write the failing test FIRST, commit, then write the code, commit.
"""
import pytest
from tip_calculator import calculate_tip, calculate_total, split_bill


def test_calculate_tip_basic():
    # RED first: this fails until you implement calculate_tip
    assert calculate_tip(100, 15) == 15.0

# TODO: add your own tests below (fixture, parametrize, edge cases).
