from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    '''(Dict ,Dict,number) -> Dict
    '''
    gladiator = {
        'health': health,
        'rage': rage,
        'damage low': damage_low,
        'damage high': damage_high
    }
    return gladiator


def attack(attacker, defender):
    damage_dealt = randint(attacker['damage low'], attacker['damage high'])
    critical = damage_dealt * 2
    if attacker['rage'] > randint(1, 100):
        defender['health'] = defender['health'] - critical

    else:
        defender['health'] = defender['health'] - damage_dealt
        defender['health'] = max(defender['health'], 0)
        attacker['rage'] = attacker['rage'] + 15
    return defender['health']


def heal(gladiator):
    if gladiator['rage'] >= 10:
        gladiator['rage'] = gladiator['rage'] - 10
        health = gladiator['health'] + 5
        gladiator['health'] = min(100, health)
    else:
        gladiator['rage'] == 0


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
    else:
        return False


def main():
    new_gladiator()


if __name__ == '__main__':
    main()
