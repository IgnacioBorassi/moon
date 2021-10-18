from barco import Barco


class civilizacion:
    def __init__(self):
        self.cantMadera = 0
        self.cantPiedra = 0
        self.barco = Barco()
        self.obreros = []
        self.guerreros = []
        self.arqueros = []
    
    def getMadera(self):
        return self.cantMadera

    def restarMadera(self, cant):
        self.cantMadera -= cant
        print(self.cantMadera)

    def restarPiedra(self, cant):
        self.cantPiedra -= cant
        print(self.cantPiedra)
    
    def agregarMadera(self, cant):
        self.cantMadera += cant
        print(self.cantMadera)
    
    def getPiedra(self):
        return self.cantPiedra
    
    def agregarPiedra(self, cant):
        self.cantPiedra += cant
    
    def CrearBarco(self):
        print(self.cantMadera)
        if self.cantMadera >= 20:
            self.barco.Crear()
            self.restarMadera(20)
        else:
            print("agarra madera")
            
        
    def getBarco(self):
        return self.barco.getBarco()
    
    def restarUsoBarco(self):
        self.barco.restarUsos()
    
    def getUsosBarco(self):
        return self.barco.getUsos()
    
    def hacerCasa(self):
        if self.cantMadera >= 40 and self.cantPiedra >= 20:
            self.restarMadera(40)
            self.restarPiedra(20)
        else:
            print("te faltan recursos panflin")
    