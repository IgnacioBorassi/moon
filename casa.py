class Casa:
    def __init__(self, activo):
        '''Representa la casa de los pelados'''
        self.activo = activo
        
    

    def ponerCasa(self):
        self.activo = True
    
    def getCasa(self):
        return self.activo

    def __repr__(self) -> str:
        return "Casa"