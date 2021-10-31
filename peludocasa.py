class PeludoCasa:
    def __init__(self, activo):
        """La casa de los enemigos de los pelados que son peludos"""
        self.activo = activo
        
    

    def ponerPeludoCasa(self):
        self.activo = True
    
    def getPeludoCasa(self):
        return self.activo

    def __repr__(self) -> str:
        return "PeludoCasa"