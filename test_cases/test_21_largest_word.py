from codes.largest_word import largest_word


def test_simple_sentence():
    assert largest_word("I love programming") == "programming"


def test_punctuation_is_ignored():
    assert largest_word("Hello, world!") == "Hello"


def test_tie_returns_first_word():
    assert largest_word("cat dog bat") == "cat"


def test_single_word():
    assert largest_word("Python") == "Python"


def test_empty_sentence():
    assert largest_word("") == ""