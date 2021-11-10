import random
class Cultivo:
    '''El cultivo como construccion, otorga comida'''

    def __init__(self, activo):
        """Representa un cultivo que te da comida"""
        self.activo = activo
    

    def ponerCultivo(self):
        self.activo = True
    
    def getCultivo(self):
        return self.activo

    def randomMaterial(self):
        '''Otorga una cantidad aleatoria del material correspondiente'''
        num = random.randrange(5, 10)
        return num

    def __repr__(self) -> str:
        return "Cultivo"