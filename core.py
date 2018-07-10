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
    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    critical = damage_dealt * 2
    if attacker['rage'] > randint(1, 100):
        defender['health'] = defender['health'] - critical

    else:
        defender['health'] = defender['health'] - damage_dealt
        defender['health'] = max(defender['health'], 0)
        attacker['rage'] = attacker['rage'] + 15
    return defender[health]


def healer(gladiator):
    pass


def is_dead(gladiator):
    pass


def main():
    new_gladiator()


if __name__ == '__main__':
    main()
