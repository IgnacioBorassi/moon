from sibilisasion import civilizacion

class Jugador:
    def __init__(self):
        self.energia = 500
        self.comida = 30
        self.civilizacion = civilizacion()
    
    def getMadera(self):
        return self.civilizacion.getMadera()
    
    def getPiedra(self):
        return self.civilizacion.getPiedra()
    
    def getEnergia(self):
        return self.energia

    def getComida(self):
        return self.comida

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
    
    def restarComida(self, cant):
        self.comida -= cant
        if self.comida < 0:
            self.comida = 0
            
    def setEnergia(self):
        self.energia = 500

    def setComida(self):
        self.comida = 30

    def crearBarco(self):
        self.civilizacion.CrearBarco()

    def getMadera(self):
        return self.civilizacion.getMadera()

    def restarMadera(self, cant):
        self.civilizacion.restarMadera(cant)

    
    def agregarComida(self, cant):
        self.civilizacion.agregarComida(cant)

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
    
    def getFundadorActivo(self):
        return self.civilizacion.getFundadorActivo()

    def getGuerrerorActivo(self):
        return self.civilizacion.getGuerrerorActivo()
    
    def getArqueroActivo(self):
        return self.civilizacion.getArqueroActivo()
    
    def getObreroActivo(self):
        return self.civilizacion.getObreroActivo()
    
    def matarFundador(self):
        self.civilizacion.matarFundador()
    
    def ponerGuerrero(self):
        self.civilizacion.ponerGuerrero()
    
    def ponerArquero(self):
        self.civilizacion.ponerArquero()
    
    def ponerObreros(self):
        self.civilizacion.ponerObreros()

    def hacerPuerto(self):
        self.civilizacion.hacerPuerto()
    
    def hacerMina(self):
        self.civilizacion.hacerMina()
