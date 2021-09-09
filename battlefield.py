from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.winner = ''
    
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
        total_robot_health = self.get_total_robot_health()
        total_dino_health = self.get_total_dino_health()
        round = 1
        while total_dino_health > 0 and total_robot_health > 0:
            print('--------------------------------------------')
            print('\nRound ', round)
            #Dino turn
            self.dino_turn()

            total_robot_health = self.get_total_robot_health()
            total_dino_health = self.get_total_dino_health()
            if total_dino_health <= 0 and total_robot_health <= 0:
                break

            #Robot turn
            self.robo_turn()
            total_robot_health = self.get_total_robot_health()
            total_dino_health = self.get_total_dino_health()
            round += 1
            

    def get_total_robot_health(self):
        total_robot_health = self.fleet.robots[0].health + self.fleet.robots[1].health + self.fleet.robots[2].health
        if total_robot_health == 0:
            self.winner = 'dinos'
        return total_robot_health
         
    
    def get_total_dino_health(self):
        total_dino_health =  self.herd.dinosaurs[0].health + self.herd.dinosaurs[1].health + self.herd.dinosaurs[2].health
        if total_dino_health == 0:
            self.winner = 'robots'
        return total_dino_health

    def dino_turn(self):
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
        

    def robo_turn(self):
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
        if self.winner == 'dinos':
            print('\n\nThe dinosaurs have defeated the robots')
        elif self.winner == 'robots':
            print('\n\nThe robots have defeated the dinos')