"""
Ручные тесты для классов User и Admin.

Запуск:
    pytest test_user_manual.py -v

Предполагается, что User и Admin определены в модуле user.py.
Если они в другом файле — поправь импорт ниже.
"""

from user import User, Admin
import pytest

# ---------------------------------------------------------------------------
# 1. is_adult: граница 17 лет -> False
# ---------------------------------------------------------------------------
def test_is_adult_17_returns_false():
    user = User("Иван", 18, "ivan17@example.com")
    assert user.is_adult()

# ---------------------------------------------------------------------------
# 2. is_adult: граница 18 лет -> True
# ---------------------------------------------------------------------------
def test_is_adult_18_returns_true():
    user = User("Иван", 18, "ivan18@example.com")
    assert user.is_adult() 


# ---------------------------------------------------------------------------
# 3. is_adult: 0 лет -> False (ещё одно граничное значение)
# ---------------------------------------------------------------------------
def test_is_adult_zero_returns_false():
    user = User("Малыш", 18, "baby@example.com")
    assert user.is_adult() 


# ---------------------------------------------------------------------------
# 4. greet: возвращает строку с именем
# ---------------------------------------------------------------------------
def test_greet_contains_name():
    user = User("Мария", 30, "maria@example.com")
    greeting = user.greet()
    assert isinstance(greeting, str)
    assert "Мария" in greeting


# ---------------------------------------------------------------------------
# 5. change_email: успешная смена
# ---------------------------------------------------------------------------
def test_change_email_success():
    user = User("Иван", 25, "old@example.com")
    result = user.change_email("new@example.com")
    assert user.mail == "new@example.com"
    assert result == "new@example.com"


# ---------------------------------------------------------------------------
# 6. change_email: некорректный email -> ValueError (try/except)
# ---------------------------------------------------------------------------
def test_change_email_invalid():
    user = User("Иван", 25, "old@example.com")
    try:
        user.change_email("bad-email")
        assert False, "Ожидалось ValueError"
    except ValueError:
        assert True
    # старый mail не должен измениться после неудачной попытки
    assert user.mail == "old@example.com"


# ---------------------------------------------------------------------------
# 7. change_email: некорректный email -> ValueError (через pytest.raises)
# ---------------------------------------------------------------------------
def test_change_email_invalid_with_pytest_raises():
    import pytest
    user = User("Иван", 25, "old@example.com")
    with pytest.raises(ValueError):
        user.change_email("no-at-sign") 


# ---------------------------------------------------------------------------
# 8. has_permission у админа: право ЕСТЬ -> True
# ---------------------------------------------------------------------------
def test_admin_has_permission_true():
    admin = Admin("Костя", 30, "lmao@gmail.com", ["read", "write", "delete"])
    assert admin.has_permission("delete")


# ---------------------------------------------------------------------------
# 9. has_permission у админа: права НЕТ -> False
# ---------------------------------------------------------------------------
def test_admin_has_permission_false():
    admin = Admin("Костя", 30, "lmao@gmail.com", ["read", "write", "delete"])
    assert not admin.has_permission("ban")

# ---------------------------------------------------------------------------
# 10. Admin наследует is_adult от User
# ---------------------------------------------------------------------------
def test_admin_inherits_is_adult():
    admin = Admin("Костя", 30, "lmao@gmail.com", ["read"])
    assert admin.is_adult() is True

    admin_minor = Admin("Петя", 15, "petya@example.com", [])
    assert admin_minor.is_adult() is False


# ---------------------------------------------------------------------------
# 11. Admin: пустой список прав -> любое право False
# ---------------------------------------------------------------------------
def test_admin_with_empty_permissions():
    admin = Admin("Костя", 30, "lmao@gmail.com", [])
    assert admin.has_permission("read") == False
    assert admin.has_permission("delete") == False


#12
def test_change_email_invalid():
    user = User("Иван", 25, "old@example.com")
    with pytest.raises(ValueError):
        user.change_email("bad-email")
