import pytest

@pytest.mark.parametrize("input, output", [(1,11), (2, 22), (3, 33)])
def test_multiplication(input, output):
    assert 11*input == output