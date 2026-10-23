"""Test cases for Program 29."""

import importlib

is_armstrong = importlib.import_module(
    "codes.29_armstrong_number"
).is_armstrong


def test_three_digit_armstrong():
    assert is_armstrong(153) is True


def test_another_armstrong_number():
    assert is_armstrong(370) is True


def test_non_armstrong_number():
    assert is_armstrong(123) is False


def test_zero():
    assert is_armstrong(0) is True


def test_negative_number():
    assert is_armstrong(-153) is False