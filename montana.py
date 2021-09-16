import random

class Montana:
    '''Representa el montana y su material'''

    def __init__(self):
        self.material = self.randomMaterial()

    def randomMaterial(self):
        '''Proximamente'''
        num = random.randrange(100, 121)
        return num