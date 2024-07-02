import pytest

@pytest.mark.dev
def test_dict():
    empdata = {"no" : 1001, "ename": "Ishwarya", "esal": 2000}
    assert empdata['esal'] == 2000

@pytest.mark.prod
def test_firstCreditCard():
    print("First Credit card")

def test_secondCreditCard():
    print("Second Credit Card")