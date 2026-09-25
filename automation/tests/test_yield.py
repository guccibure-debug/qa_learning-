import os
import pytest

@pytest.fixture
def temp_file():
    path = "temp_test_file.txt"
    with open (path, "w") as f:
        f.write("hello")

    yield path

    os.remove(path)

def test_read(temp_file):
    with open(temp_file) as f:
        assert f.read() == "hello"
