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
def test_calculate_total_basic():
       assert calculate_total(100, 15) == 115.0

def test_split_bill_basic():
       assert split_bill(115, 2) == 57.5       

def test_calculate_tip_negative_bill():
       with pytest.raises(ValueError):
           calculate_tip(-50, 15)


def test_calculate_tip_negative_pct():
       with pytest.raises(ValueError):
           calculate_tip(100, -5)


def test_split_bill_zero_people():
       with pytest.raises(ValueError):
           split_bill(100, 0)

@pytest.fixture
def sample_bill():
       return 100


def test_calculate_total_with_fixture(sample_bill):
       assert calculate_total(sample_bill, 20) == 120.0


@pytest.mark.parametrize("bill, tip_pct, expected", [
       (100, 15, 15.0),
       (50, 20, 10.0),
       (200, 10, 20.0),
       (80, 0, 0.0),
   ])
def test_calculate_tip_parametrized(bill, tip_pct, expected):
       assert calculate_tip(bill, tip_pct) == expected


def test_split_bill_rounds_to_two_decimals():
       assert split_bill(100, 3) == 33.33