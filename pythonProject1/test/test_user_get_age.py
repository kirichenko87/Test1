from tkinter.font import names

import  pytest
from user import User


@pytest.mark.parametrize('age, expected_result', [
    (23, 23),
    (1, 1),
    (90, 90)
])

def test_user_get_age_positive(age, expected_result):
    assert User('Garry', age).get_age() == expected_result

@pytest.mark.parametrize('age, expected_result', [
    ('dfgh', TypeError),
    ([], TypeError),
    ({'Gera': 123}, TypeError),
    (-1, ValueError),
    (101, ValueError)
])

def test_user_get_age_negative(age, expected_result):
    with pytest.raises(expected_result):
        User('Garry',age).get_age()

@pytest.mark.parametrize('age, expected_result',[
    (1, 1),
    (99, 99)
])

def test_user_get_age_limit(age, expected_result):
    assert User('Garry', age).get_age() == expected_result