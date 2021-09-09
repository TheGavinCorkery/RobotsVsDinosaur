
class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = 8
        self.health = 30

    def attack(self, robot):
        if robot.health < self.attack_power:
            robot.health = 0
        else:
            robot.health = robot.health - self.attack_power
        print('\nThe dinosaurs attack did', self.attack_power, 'damage to the robot')