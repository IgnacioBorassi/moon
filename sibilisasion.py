class civilizacion:
    def __init__(self):
        self.cantMadera = 0
        self.cantPiedra = 0
        self.barco = None
        self.obreros = []
        self.guerreros = []
        self.arqueros = []
    
    def getMadera(self):
        return self.cantMadera

    def restarMadera(self, cant):
        self.cantMadera -= cant
        print(self.cantMadera)
    
    def agregarMadera(self, cant):
        self.cantMadera += cant
        print(self.cantMadera)
    
    def getPiedra(self):
        return self.cantPiedra
    
    def agregarPiedra(self, cant):
        self.cantPiedra += cant
        print(self.cantPiedra)
    
    def restarPiedra(self, cant):
        self.cantPiedra -= cant
    
    def CrearBarco(self):
        print(self.cantMadera)
        if self.cantMadera >= 20:
            self.barco = True
            print("cree barco")
            self.restarMadera(20)
        else:
            self.barco = False