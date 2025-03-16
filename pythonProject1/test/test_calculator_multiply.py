import pytest
from calculator import Calculator


@pytest.mark.parametrize('value1, value2, expected_result', [
    (1, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (2, 2, 4),
    (3.33, 2, 6.66),
    (2, 0, 0)

])
def test_calculator_multiply_positive(value1, value2, expected_result):
    calc = Calculator()
    assert round(calc.multiply(value1, value2), 2) == expected_result


@pytest.mark.parametrize('value1, value2, expected_result', [
    ('1', '1', TypeError),
    ('10', 10, TypeError),
    (10, '1.1', TypeError),
    ('1.1', '2.2', TypeError),
    ([3.33], 2.22, TypeError)

])
def test_calculator_multiply_negative(value1, value2, expected_result):
    calc = Calculator()
    with pytest.raises(expected_result):
        calc.multiply(value1, value2)


@pytest.mark.parametrize('value1, value2, expected_result', [
    (0, 0, 0),
    (0.0, 0.0, 0),
    (1, 0.0, 0),
    (0, 1, 0)
])
def test_calculator_multiply_limit(value1, value2, expected_result):
    calc = Calculator()
    assert calc.multiply(value1, value2) == expected_result
