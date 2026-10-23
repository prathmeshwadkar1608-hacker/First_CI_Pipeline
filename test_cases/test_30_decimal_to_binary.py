"""Test cases for Program 30."""

import importlib
import pytest

decimal_to_binary = importlib.import_module(
    "codes.30_decimal_to_binary"
).decimal_to_binary


def test_decimal_ten():
    assert decimal_to_binary(10) == "1010"


def test_decimal_zero():
    assert decimal_to_binary(0) == "0"


def test_decimal_one():
    assert decimal_to_binary(1) == "1"


def test_decimal_fifteen():
    assert decimal_to_binary(15) == "1111"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)