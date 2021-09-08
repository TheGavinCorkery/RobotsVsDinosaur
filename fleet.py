from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot('Galactus')
        robot_two = Robot('Terminator')
        robot_three = Robot('Galaga')
        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)
        