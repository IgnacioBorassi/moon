class Peludo:
    '''Representa a los enemigos que tienen pelo'''

    def __init__(self):
        self.activo = None


    def activar(self):
        self.activo = True

    def getActivo(self):
        return self.activo
    
    def __repr__(self) -> str:
        return "Peludo"