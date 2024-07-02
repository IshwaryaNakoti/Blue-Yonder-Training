import pytest
def square(x):
    return x*x
def test_sqaure():
    assert square(4) == 16

@pytest.mark.xfail
def test_ename():
    name = "hari"
    assert name in "Welcome har"

def testm1():
    l1 = ['apple', 'ball', 'call']
    assert l1[0] == 'apple'