from barco import Barco
from fundador import Fundador
from guerrero import Guerrero
from arquero import Arquero
from obrero import Obrero


class civilizacion:
    '''Representa todo lo que tiene la civilizacion como la cant de madera, piedra, si tiene barco y 
    si tienen fundador, obrero, guerrero o arqueros'''

    def __init__(self):
        self.cantMadera = 0
        self.cantPiedra = 0
        self.barco = Barco()
        self.fundador = Fundador()
        self.obreros = Obrero()
        self.guerreros = Guerrero()
        self.arqueros = Arquero()
    
    def getMadera(self):
        return self.cantMadera

    def restarMadera(self, cant):
        self.cantMadera -= cant

    def restarPiedra(self, cant):
        self.cantPiedra -= cant
    
    def agregarMadera(self, cant):
        self.cantMadera += cant

    def getPiedra(self):
        return self.cantPiedra

    
    def agregarPiedra(self, cant):
        self.cantPiedra += cant

    def CrearBarco(self):
        if self.cantMadera >= 20:
            self.barco.Crear()
            self.restarMadera(20)
        else:
            print("Agarra madera")
        
    def agregarUsoBarco(self, cant):
        self.barco.agregarUsos(cant)

    def getBarco(self):
        return self.barco.getBarco()  

    def getUsosBarco(self):
        return self.barco.getUsos()

    def restarUsoBarco(self):
        self.barco.restarUsos()
    
    def hacerCasa(self):
        if self.cantMadera >= 40 and self.cantPiedra >= 20:
            self.restarMadera(40)
            self.restarPiedra(20)
        else:
            print("Te faltan recursos para hacer una casa, panflin")
    
    def getFundadorActivo(self):
        return self.fundador.getActivo()
    
    def getGuerrerorActivo(self):
        return self.guerreros.getActivo()
    
    def getArqueroActivo(self):
        return self.arqueros.getActivar()
    
    def getObreroActivo(self):
        return self.obreros.getActivo()
    
    def matarFundador(self):
        self.fundador.muerte()
    
    def ponerGuerrero(self):
        self.guerreros.vivir()
    
    def ponerArquero(self):
        self.arqueros.activar()
    
    def ponerObreros(self):
        self.obreros.activar()

    def hacerPuerto(self):
        if self.cantMadera >= 100:
            self.restarMadera(100)
        else:
            print("Te faltan recursos para hacer un puerto,  panflin")

    def hacerCorral(self):
        if self.cantMadera >= 20:
            self.restarMadera(20)
        else:
            print("Te faltan recursos para hacer un corral, panflin")

    def hacerCultivo(self):
        if self.cantMadera >= 5 and self.cantPiedra >= 3:
            self.restarMadera(5)
            self.restarPiedra(5)
        else:
            print("Te faltan recursos para hacer un cultivo, panflin")

    def hacerMina(self):
        if self.cantMadera >= 40:
            self.restarMadera(40)
        else:
            print("Te faltan recursos para hacer una mina, panflin")

    def reiniciarRecursos(self):
        self.barco.usos = 0
        self.cantPiedra = 0
        self.cantMadera = 0
    
