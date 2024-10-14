import pytest
from lab1 import card_check


def test_luhn_algorithm():
    assert card_check("4539 1488 0343 6467", "12/25", "123") == True
    assert card_check("1234 5678 9876 5432", "12/25", "123") == False


def test_expiry_date():
    assert card_check("4539 1488 0343 6467", "12/25", "123") == True
    assert card_check("4539 1488 0343 6467", "12/19", "123") == False


def test_cvc_validation():
    assert card_check("4539 1488 0343 6467", "12/25", "123") == True
    assert card_check("4539 1488 0343 6467", "12/25", "12") == False
