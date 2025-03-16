import pytest
from array1 import Array

@pytest.mark.parametrize('value, expected_result', [
    ([1, 2, 3, 4, 5], 15),
    ([0, 0, 0, 0, 0, 0], 0),
    ([-1, -2, -3, -4, -5], -15),
    ([1.2, 1, 0, 1.3], 3.5)
])
def test_array_sum_pisitive(value, expected_result):
    assert  Array(*value).sum() == expected_result

@pytest.mark.parametrize('value, expected_result',[
    ("1,2,3,4,5", TypeError),
    (('', 1), TypeError),
    (('12', 0), TypeError),
    ((None, -1), TypeError),
    (('10', '45'), TypeError),
    (([], []), TypeError),

])

def test_array_sum_negative(value, expected_result):
    with pytest.raises(expected_result):
        Array(*value).sum()

@pytest.mark.parametrize('value, expected_result',[
    ([1], 1),
    ([0], 0),
    ([-1], -1)
])

def test_array_sum_limit(value, expected_result):

    assert Array(*value).sum() == expected_result