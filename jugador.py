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
