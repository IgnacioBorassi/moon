import random
class Corral:
    def __init__(self, activo):
        """Representa un corral que te da comida"""
        self.activo = activo
    

    def ponerCorral(self):
        self.activo = True
    
    def getCorral(self):
        return self.activo

    def randomMaterial(self):
        num = random.randrange(5, 10)
        return num

    def __repr__(self) -> str:
        return "Corral"