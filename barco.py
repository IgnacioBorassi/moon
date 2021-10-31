class Barco:
    def __init__(self):
        """Es un objeto barco que tiene los usos solo si es creado"""
        self.creado = False
        self.usos = 0

    def Crear(self):
        self.creado = True
        self.usos += 10
    
    def restarUsos(self):
        self.usos -= 1
        if self.usos == 0:
            self.creado = False
        
    def agregarUsos(self, cant):
        self.usos += cant
    
    def getUsos(self):
        return self.usos
    
    def getBarco(self):
        return self.creado

    def cambiarBarcos(self, bool):
        self.creado = bool