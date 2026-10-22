import sys
from pathlib import Path
from importlib import import_module

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "codes")
)

module = import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_normal_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_first_list_empty():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_second_list_empty():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_both_lists_empty():
    assert merge_sorted_lists([], []) == []


def test_duplicate_elements():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 3]) == [1, 2, 2, 2, 3, 3]


def test_different_lengths():
    assert merge_sorted_lists([1, 10], [2, 3, 4, 5]) == [1, 2, 3, 4, 5, 10]


# python -m pytest .\test_cases\test_24_merge_sorted_lists.pys