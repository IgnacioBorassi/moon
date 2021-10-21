class Mina:
    def __init__(self, activo):
        self.activo = activo
    

    def ponerMina(self):
        self.activo = True
    
    def getMina(self):
        return self.activo

    def __repr__(self) -> str:
        return "Mina"