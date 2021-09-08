from fleet import Fleet
from herd import Herd
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.fleet.create_fleet()
        self.herd.create_herd()
        #Display welcome
        self.display_welcome()
        #battle
        #display winner
        

    def display_welcome(self):
        print('Welcome to the battle between dinosaurs and robots. ')
        print('Your job is to interact with the console in order to fight with the dinosaurs and the robots')
        


    def battle(self):
        #Dino turn
        #Robot turn
        #Repeat
        pass

    def dino_turn(self, dinosaur):
        #show dino options
        #get which dino they want to use
        #show robo options
        #get which robot to attack
        pass

    def robo_turn(self, robot):
        #show dino options
        #get which dino they want to use
        #show robo options
        #get which robot to attack
        robot.attack()
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass