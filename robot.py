from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 20
        self.weapon = Weapon

    def attack(self, dinosaur):
        pass