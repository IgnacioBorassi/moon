class Fundador:
    def __init__(self):
        self.activo = None
       
    
    def fundarCivilizacion(self):
        self.fundar = True
    
    def activar(self):
        self.activo = True
    
    def muerte(self):
        self.activo = False
    
    def getActivo(self):
        return self.activo
    
    def __repr__(self) -> str:
        return "Fundador"
