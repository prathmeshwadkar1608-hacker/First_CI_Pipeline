import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codes"))

from importlib import import_module

module = import_module("23_sort_without_sort")
bubble_sort = module.bubble_sort


def test_normal_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_already_sorted_list():
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_sorted_list():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicate_numbers():
    assert bubble_sort([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]


def test_original_list_unchanged():
    numbers = [5, 2, 9, 1]
    bubble_sort(numbers)
    assert numbers == [5, 2, 9, 1]


def test_empty_list():
    assert bubble_sort([]) == []

# python -m pytest .\test_cases\test_23_sort_without_sort.py