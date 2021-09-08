from dinosaur import Dinosaur
from robot import Robot
from herd import Herd
from fleet import Fleet

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

