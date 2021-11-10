class Barco:
    '''Es un objeto barco que tiene los usos solo si es creado'''

    def __init__(self):  
        self.creado = False
        self.usos = 0


    def Crear(self):
        '''Crea 10 unidades utilizables de Barco'''
        self.creado = True
        self.usos += 10
    
    def restarUsos(self):
        '''Resta la cantidad de usos totales'''
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