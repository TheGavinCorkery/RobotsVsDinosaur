from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dino_one = Dinosaur('Teddy')
        dino_two = Dinosaur('Ralph')
        dino_three = Dinosaur('Hendrix')
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        