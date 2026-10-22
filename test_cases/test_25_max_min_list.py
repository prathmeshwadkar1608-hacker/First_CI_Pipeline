import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codes"))

from importlib.util import spec_from_file_location, module_from_spec

file_path = Path(__file__).resolve().parents[1] / "codes" / "25_max_min_list.py"
spec = spec_from_file_location("max_min_module", file_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

find_max_min = module.find_max_min

def test_normal_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -9, -1]) == (-1, -9)


def test_duplicate_numbers():
    assert find_max_min([4, 4, 4]) == (4, 4)


def test_single_element():
    assert find_max_min([7]) == (7, 7)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])

# python -m pytest .\test_cases\test_25_max_min_list.py