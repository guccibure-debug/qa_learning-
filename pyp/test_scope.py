import pytest

@pytest.fixture(scope="module")
def module_counter():
    """счетчик живущий весь модуль"""
    print("\n>>>СОЗДАЁМ счётчик")
    counter = {"value":0}
    yield counter 
    print("\n>>>УНИЧТОЖАЕМ счётчик")

@pytest.fixture
def function_counter():
    """счётчик создаваемый для каждого теста"""
    print("\n>>>создаём счётчик")
    counter = {"value":0}
    yield counter 
    print("\n>>>уничтожаем счётчик")

def test_module_first(module_counter):
    module_counter["value"] += 1
    print(f"module_counter = {module_counter['value']}")
    assert module_counter["value"] >= 1

def test_module_second(module_counter):
    module_counter["value"] += 1
    print(f"module_counter = {module_counter['value']}")
    assert module_counter["value"] >= 2    #значение сохранилось между тестами

def test_function_first(function_counter):
    function_counter["value"] += 1
    print(f"function_counter = {function_counter['value']}")
    assert function_counter["value"] == 1 

def test_function_second(function_counter):
    function_counter["value"] += 1
    print(f"function_counter = {function_counter['value']}")
    assert function_counter["value"] == 1   #значение сброшено