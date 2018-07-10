from core import *


def test_new_gladiator():
    assert new_gladiator(100, 0, 1, 100) == {
        'health': 100,
        'rage': 0,
        'damage low': 1,
        'damage high': 100
    }
    assert new_gladiator(100, 25, 5, 25) == {
        'health': 100,
        'rage': 25,
        'damage low': 5,
        'damage high': 25
    }
