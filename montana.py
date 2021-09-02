import random
class Montana:
    def __init__(self):
        self.material = self.randomMaterial()

    def randomMaterial(self):
        num = random.randrange(100, 121)
        return num