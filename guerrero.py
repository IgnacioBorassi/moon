class Guerrero:
    '''Un tipo de persona'''
    
    def __init__(self):
        self.activo = None
        self.atacar = None
    
    def atacar(self):
        self.atacar = True
    
    def vivir(self):
        self.activo = True
    
    def morir(self):
        self.activo= False
    
    def getActivo(self):
        return self.activo
    
    def __repr__(self) -> str:
        return "Guerrero"