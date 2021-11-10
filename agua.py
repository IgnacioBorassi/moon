import random
class Agua:
    '''Representa el agua y su contrucciones'''
    
    def __init__(self, naturaleza, construccion):
        self.naturaleza = naturaleza
        self.construccion = construccion


    def getNaturaleza(self):
        return self.naturaleza

    def setConstruccion(self):
        self.construccion = True

    def getConstruccion(self):
        return self.construccion

    def __repr__(self) -> str:
        return "Agua"
    
    def randomMaterial(self):
        '''Otorga una cantidad aleatoria del material correspondiente'''
        num = random.randrange(1, 10)
        return num