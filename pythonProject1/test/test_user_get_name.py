from tkinter.font import names

import  pytest
from user import User


@pytest.mark.parametrize('name, expected_result', [
    ('Mark', 'Mark'),
    ('Fedor', 'Fedor'),
    ('Lary', 'Lary')
])

def test_user_get_name_positive(name, expected_result):
    assert User(name, 25).get_name() == expected_result

@pytest.mark.parametrize('name, expected_result', [
    (123, TypeError),
    ([], TypeError),
    ({'Gera': 123}, TypeError),
    ('',ValueError),
    ('123',ValueError)
])

def test_user_get_name_negative(name, expected_result):
    with pytest.raises(expected_result):
        User(name,24).get_name()

@pytest.mark.parametrize('name, expected_result',[
    ('A', 'A'),
    ('aa', 'aa')
])

def test_user_get_name_limit(name, expected_result):
    assert User(name, 9).get_name()