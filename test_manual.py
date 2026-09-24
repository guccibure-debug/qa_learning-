from qa_lear.basics import is_even, get_max, reverse_string

def test_is_even_true():
    """Позитивный тест: чётное число."""
    assert is_even(2) is True

def test_is_even_false():
    """Негативный тест: нечётное число."""
    assert is_even(3) is False

def test_get_max_normal():
    """Максимум в списке одного элемента"""
    assert (get_max([2,3,4,5,6,7,8,9])) == 9

def test_get_max_single():
    """максимум в списке из одного элемента"""
    assert get_max([42]) == 42

def test_get_max_empty():
    """пустой список - none"""
    assert get_max([]) == None

def test_reverse_string_regular():
    assert reverse_string("Hello") == "olleH"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_single():
    assert reverse_string("a") == "a"

if __name__ == "__main__":
    test_is_even_true()
    test_is_even_false()
    test_get_max_normal()
    test_get_max_single()
    test_get_max_empty()
    test_reverse_string_regular()
    test_reverse_string_empty()
    test_reverse_string_single()
    print("Все тесты прошли!")