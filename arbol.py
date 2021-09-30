import random

class Arbol:
    '''Representa el arbol y su material'''

    def __init__(self):
        self.material = self.randomMaterial()


    def randomMaterial(self):
        num = random.randrange(10, 100)
        return num

        