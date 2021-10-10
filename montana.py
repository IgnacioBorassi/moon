import random

class Montana:
    '''Representa el montana y su material'''

    def __init__(self):
        self.material = self.randomMaterial()

    def randomMaterial(self):
        num = random.randrange(10, 100)
        return num

    def _repr_(self) -> str:
        return "Montana"