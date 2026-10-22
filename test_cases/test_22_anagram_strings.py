from codes.anagram_strings import is_anagram


def test_anagram_strings():
    assert is_anagram("Listen", "Silent") == True


def test_different_strings():
    assert is_anagram("hello", "world") == False


def test_uppercase_and_lowercase():
    assert is_anagram("LISTEN", "silent") == True


def test_strings_with_spaces():
    assert is_anagram("Dormitory", "Dirty room") == True


def test_empty_strings():
    assert is_anagram("", "") == True