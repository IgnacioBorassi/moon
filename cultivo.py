import random
class Cultivo:
    def __init__(self, activo):
        self.activo = activo
    

    def ponerCultivo(self):
        self.activo = True
    
    def getCultivo(self):
        return self.activo

    def randomMaterial(self):
        num = random.randrange(5, 10)
        return num

    def __repr__(self) -> str:
        return "Cultivo"