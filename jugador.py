from sibilisasion import civilizacion

class Jugador:
    def __init__(self):
        self.energia = 500
        self.civilizacion = civilizacion()
    
    def getMadera(self):
        return self.civilizacion.getMadera()
    
    def getPiedra(self):
        return self.civilizacion.getPiedra()
    
    def getEnergia(self):
        return self.energia

    def agregarMadera(self, cant):
        self.civilizacion.agregarMadera(cant)
    
    def restarMadera(self,cant):
        self.civilizacion.restarMadera(cant)
    
    def agregarPiedra(self, cant):
        self.civilizacion.agregarPiedra(cant)
    
    def restarPiedra(self, cant):
        self.civilizacion.restarMadera(cant)

    def restarEnergia(self, cant):
        self.energia -= cant
        if self.energia < 0:
            self.energia = 0
        
            
    
    def setEnergia(self):
        self.energia = 500

    def crearBarco(self):
        self.civilizacion.CrearBarco()

    def getMadera(self):
        return self.civilizacion.getMadera()

    def restarMadera(self, cant):
        self.civilizacion.restarMadera(cant)

    
    def agregarPiedra(self, cant):
        self.civilizacion.agregarPiedra(cant)

    def restarPiedra(self, cant):
        self.civilizacion.restarPiedra(cant)

    def getEnergia(self):
        return self.energia

    def getBarco(self):
        return self.civilizacion.getBarco()
    
    def restarUsoBarco(self):
        self.civilizacion.restarUsoBarco()

    def getUsosBarco(self):
        return self.civilizacion.getUsosBarco()
    
    def hacerCasa(self):
        self.civilizacion.hacerCasa()