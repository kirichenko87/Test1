import pytest
from calculator import Calculator


@pytest.mark.parametrize('value1, value2, expected_result', [
    (1, 1, 0),
    (10, 10, 0),
    (10, 1.1, 8.9),
    (2.1, 2, 0.1),
    (3.33, 2.22, 1.11),
    (2, 0, 2)

])
def test_calculator_subtract_positive(value1, value2, expected_result):
    calc = Calculator()
    assert round(calc.subtract(value1, value2), 2) == expected_result


@pytest.mark.parametrize('value1, value2, expected_result', [
    ('1', '1', TypeError),
    ('10', 10, TypeError),
    (10, '1.1', TypeError),
    ('1.1', '2.2', TypeError),
    ([3.33], 2.22, TypeError)

])
def test_calculator_subtract_negative(value1, value2, expected_result):
    calc = Calculator()
    with pytest.raises(expected_result):
        calc.subtract(value1, value2)


@pytest.mark.parametrize('value1, value2, expected_result', [
    (0, 0, 0),
    (0.0, 0.0, 0)
])
def test_calculator_subtract_limit(value1, value2, expected_result):
    calc = Calculator()
    assert calc.subtract(value1, value2) == expected_result
