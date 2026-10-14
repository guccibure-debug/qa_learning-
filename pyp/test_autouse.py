import pytest

@pytest.fixture(autouse=True)
def log_test_name(request):
    """логирует имя каждого теста до и после выполнения"""
    print(f"\n>>>начало теста: {request.node.name}")
    yield
    print(f"\n>>>конец теста: {request.node.name}")

def test_first():
    print("выполняется test_first")
    assert 1+1==2

def test_second():
    print("выполняется test_second")
    assert 2*2==4

def test_third():
    print("выполняется test_third")
    assert 10/2==5