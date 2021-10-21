class Arquero:
    def __init__(self):
        self.activo = None
    
    def activar(self):
        self.activar = True
    
    def getActivar(self):
        return self.activar
    
    def __repr__(self) -> str:
        return "Arquero"