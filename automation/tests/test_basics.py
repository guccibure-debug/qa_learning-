from automation.basics.basics import add, is_adult, multiply, is_even, get_max, count_vowels, reverse_string, reverse_string_1
import pytest

def test_add():
    assert add(2,3) == 5

def test_is_adult():
    assert is_adult(18)

def test_multiply():
    assert multiply(3,2) == 6
    assert multiply(-2,2) == -4
    assert multiply(1,2)+1 == 3

def test_is_even_true():
    assert is_even(192) is True
def test_is_even_false():
    assert is_even(191) is False
def test_is_even_error():
    with pytest.raises(ValueError):
         is_even(0)

def test_get_max():
    assert get_max([3,5,6]) == 6

def test_count_vowels():
    assert count_vowels("hello")==2
    assert count_vowels("") == 0
    assert count_vowels("приllo") == 1
    assert count_vowels("lklk") == 0

def test_reverse_string():
    assert reverse_string("строка")=="акортс"

def test_reverse_string_1():
    assert reverse_string_1("result")=="tluser"