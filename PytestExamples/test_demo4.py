import pytest

@pytest.fixture()
def m1():
    #assume this is a connection code or a file code
    return "Hi"

def test_m1(m1):
    assert m1 == "Hi"
