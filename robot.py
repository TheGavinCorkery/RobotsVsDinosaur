from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.weapon = Weapon('sword', 10)

    def attack(self, dinosaur):
        if dinosaur.health < self.weapon.attack_power:
            dinosaur.health = 0
        else:
            dinosaur.health -= self.weapon.attack_power
        print('\nThe robots attack did', self.weapon.attack_power, 'damage to the dinosaur')
        