class Barco:
    def __init__(self):
        self.creado = False
        self.usos = None

    def Crear(self):
        self.creado = True
        self.usos = 10
    
    def restarUsos(self):
        self.usos -= 1
        if self.usos == 0:
            self.creado = False
        

    def getUsos(self):
        return self.usos
    
    def getBarco(self):
        return self.creado