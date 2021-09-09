from fleet import Fleet
from herd import Herd

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
        self.battle()
        #display winner
        self.display_winners()
        

    def display_welcome(self):
        print('Welcome to the battle between dinosaurs and robots. ')
        print('Your job is to interact with the console in order to fight with the dinosaurs and the robots')
        


    def battle(self):
        total_robot_health = self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health
        total_dino_health = self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health

        while total_dino_health > 0 or total_robot_health > 0:
            #Dino turn
            self.dino_turn(self.herd.dinosaurs)
            total_robot_health = self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health
            total_dino_health = self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health
            if total_dino_health <= 0 or total_robot_health <= 0:
                break
            #Robot turn
            self.robo_turn(self.fleet.robots)
            total_robot_health = self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health
            total_dino_health = self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health
            
        

    def dino_turn(self, dinosaur):
        #show dino options
        self.show_dino_opponent_options()
        #get which dino they want to use
        attacking_dinosaur = int(input('Which dinosaur would you like to attack with? '))
        attacking_dinosaur = attacking_dinosaur - 1
        #show robo options
        self.show_robo_opponent_options()
        #get which robot to attack
        robot_to_attack = int(input('Which robot would you like to attack? '))
        robot_to_attack = robot_to_attack - 1
        self.herd.dinosaurs[attacking_dinosaur].attack(self.fleet.robots[robot_to_attack])
        

    def robo_turn(self, robot):
        #show robot options
        self.show_robo_opponent_options()
        #get which robo they want to use
        attacking_robot = int(input('Which robot would you like to attack with? '))
        attacking_robot = attacking_robot - 1
        #show dino options
        self.show_dino_opponent_options()
        #get which dino to attack
        dinosaur_to_attack = int(input('Which dinosaur would you like to attack? '))
        dinosaur_to_attack = dinosaur_to_attack - 1
        self.fleet.robots[attacking_robot].attack(self.herd.dinosaurs[dinosaur_to_attack])
        

    def show_dino_opponent_options(self):
        #Display all of the dinosaurs and their health
        print('\nDinosaurs:')
        for x in range (0, len(self.herd.dinosaurs)):
            if self.herd.dinosaurs[x].health > 0:
                print('Dinosaur ', x + 1, 'name and health: ', self.herd.dinosaurs[x].name, ' ', self.herd.dinosaurs[x].health)
        

    def show_robo_opponent_options(self):
        print('\nRobots:')
        #Display all of the robots and their health
        for x in range (0, len(self.herd.dinosaurs)):
            if self.fleet.robots[x].health > 0:
                print('Robot ', x + 1, 'name and health: ', self.fleet.robots[x].name, ' ', self.fleet.robots[x].health)
        

    def display_winners(self):
        pass