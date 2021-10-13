class Casa:
    def __init__(self, activo):
        self.activo = activo
    

    def ponerCasa(self):
        self.activo = True
    
    def getCasa(self):
        return self.activo

    def __repr__(self) -> str:
        return "Casa"