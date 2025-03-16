import pytest
from calculator import Calculator


@pytest.mark.parametrize('value1, value2, expected_result', [
    (1, 1, 1),
    (0, 1, 0),
    (2, 2, 1),
    (3.33, 2, 1.67),

])
def test_calculator_divide_positive(value1, value2, expected_result):
    calc = Calculator()
    assert round(calc.divide(value1, value2), 2) == expected_result


@pytest.mark.parametrize('value1, value2, expected_result', [

    ('10', 10, TypeError),
    (10, '1.1', TypeError),
    ('1.1', '2.2', TypeError),
    ([3.33], 2.22, TypeError)

])
def test_calculator_divide_negative(value1, value2, expected_result):
    calc = Calculator()
    with pytest.raises(expected_result):
        calc.multiply(value1, value2)


@pytest.mark.parametrize('value1, value2, expected_result', [
    (1, 1, 1),
    (-1, 1, -1)
])
def test_calculator_divide_limit(value1, value2, expected_result):
    calc = Calculator()
    assert calc.divide(value1, value2) == expected_result
