import math, pytest

def test_squareRoot():
    assert math.sqrt(4)  == 2

@pytest.mark.prod
def test_square():
    assert 4*4 == 16