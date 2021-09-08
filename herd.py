class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self, dinosaur):
        self.dinosaurs.append(dinosaur)
        print(dinosaur, ' has been added to the herd.')