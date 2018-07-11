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


def test_attack_no_highlow():
    attacker = new_gladiator(100, 0, 15, 15)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)

    assert attacker['rage'] == 15
    assert defender['health'] == 85


def test_attack_rage():
    attacker = new_gladiator(100, 100, 15, 15)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)


def test_attack_highlow():
    attacker = new_gladiator(100, 0, 15, 30)
    defender = new_gladiator(100, 0, 15, 15)
    attack(attacker, defender)


def test_heal():
    glad_1 = new_gladiator(70, 10, 29, 69)
    heal(glad_1)
    assert glad_1 == {
        'health': 75,
        'rage': 0,
        'damage low': 29,
        'damage high': 69
    }


def test_is_dead():
    gladiator = new_gladiator(100, 0, 10, 25)
    assert is_dead(gladiator) == False

    gladiator['health'] = 0
    assert is_dead(gladiator) == True
