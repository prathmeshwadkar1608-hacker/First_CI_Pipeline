"""Test cases for Program 28."""

import importlib

set_intersection = importlib.import_module(
    "codes.28_set_intersection"
).set_intersection


def test_normal_intersection():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_identical_sets():
    assert set_intersection({1, 2}, {1, 2}) == {1, 2}


def test_empty_set():
    assert set_intersection(set(), {1, 2}) == set()


def test_duplicates_in_input():
    assert set_intersection([1, 1, 2], [1, 3]) == {1}