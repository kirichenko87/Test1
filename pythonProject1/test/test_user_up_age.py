from tkinter.font import names

import  pytest
from user import User


@pytest.mark.parametrize('age, expected_result', [
    (23, 24),
    (1, 2),
    (90, 91)
])

def test_user_up_age_positive(age, expected_result):
    assert User('Garry', age).up_age() == expected_result

@pytest.mark.parametrize('age, expected_result', [
    ('dfgh', TypeError),
    ([], TypeError),
    ({'Gera': 123}, TypeError),
    (-1, ValueError),
    (101, ValueError)
])

def test_user_up_age_negative(age, expected_result):
    with pytest.raises(expected_result):
        User('Garry',age).up_age()

@pytest.mark.parametrize('age, expected_result',[
    (1, 2),
    (99, 100)
])

def test_user_gup_age_limit(age, expected_result):
    assert User('Garry', age).up_age() == expected_result