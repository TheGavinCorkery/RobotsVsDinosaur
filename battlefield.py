from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd
    
    def run_game(self):
        fleet = Fleet()
        herd = Herd()
        robot_one = Robot('Galactus')
        fleet.create_fleet(robot_one)
        robot_two = Robot('Terminator')
        fleet.create_fleet(robot_two)
        robot_three = Robot('Galaga')
        fleet.create_fleet(robot_three)

        dino_one = Dinosaur('Teddy', 5)
        herd.create_herd(dino_one)
        dino_two = Dinosaur('Ralph', 8)
        herd.create_herd(dino_two)
        dino_three = Dinosaur('Hendrix', 5)
        herd.create_herd(dino_three)

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass