from core import *


def main():
    print('Welcome to Big Man, Big Fight.com')

    print('[A]attack')
    print('[P]pass')
    print('[Q]quit')
    print('[H]heal')

    Gladiator_1 = new_gladiator(100, 5, 3, 47)
    Gladiator_2 = new_gladiator(100, 13, 18, 42)
    while True:
        if is_dead(Gladiator_1):
            print('Gladiator 2 wins')
            break
        while True:
            response = input('1: What would you like to do?').strip().upper()
            if response == 'A':
                attack(Gladiator_1, Gladiator_2)
                print(Gladiator_2)
                break
            elif response == 'P':
                print(Gladiator_2)
                break
            elif response == 'Q':
                return
            elif response == 'H':
                heal(Gladiator_1)
                break
            else:
                Gladiator_1['health'] == is_dead(Gladiator_1)
                break

        if is_dead(Gladiator_2):
            print('Gladiator 1 wins')
            break
        while True:
            response = input('2: What would you like to do?').strip().upper()
            if response == 'A':
                attack(Gladiator_2, Gladiator_1)
                print(Gladiator_1)
                break
            elif response == 'P':
                print(Gladiator_1)
                break
            elif response == 'Q':
                return
            elif response == 'H':
                heal(Gladiator_2)
                print(Gladiator_1)
                break
            else:
                Gladiator_2['health'] == is_dead(Gladiator_2)
                break


if __name__ == '__main__':
    main()
