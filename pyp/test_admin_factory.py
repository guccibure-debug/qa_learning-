import pytest
from models.model import Admin

@pytest.fixture
def admin_factory():
    """фабрика админов"""
    def _make(name="admin", age=30, email="admin@example.com", permissions=None):
        return Admin(name, age, email, permissions)
    return _make

def test_admin_default_no_permissions(admin_factory):
    admin = admin_factory()
    assert admin.permissions == []
    assert not admin.has_permission("ban")

def test_admin_with_permissions(admin_factory):
    admin = admin_factory(permissions=["ban", "delete"])
    assert admin.has_permission("ban")
    assert admin.has_permission("delete")
    assert not admin.has_permission("edit")

def test_admin_inherits_is_adult(admin_factory):
    admin = admin_factory(age=30)
    assert admin.is_adult()

def test_admin_minor_not_adult(admin_factory):
    admin = admin_factory(age=16)
    assert not admin.is_adult()


