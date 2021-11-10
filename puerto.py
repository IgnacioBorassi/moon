class Puerto:
    '''Representa un puerto que va en el agua'''
    
    def __init__(self, activo):
        self.activo = activo
    

    def ponerPuerto(self):
        self.activo = True
    
    def getPuerto(self):
        return self.activo

    def __repr__(self) -> str:
        return "Puerto"