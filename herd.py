from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dino_one = Dinosaur('Teddy', 5)
        dino_two = Dinosaur('Ralph', 8)
        dino_three = Dinosaur('Hendrix', 5)
        self.dinosaurs.append(dino_one)
        self.dinosaurs.append(dino_two)
        self.dinosaurs.append(dino_three)
        