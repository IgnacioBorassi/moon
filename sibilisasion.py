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
<<<<<<< HEAD
=======
        print(self.cantPiedra)
    
    def restarPiedra(self, cant):
        self.cantPiedra -= cant
>>>>>>> 08162da4706f5676ca9da513a53c6aef0e2b4c55
    
    def CrearBarco(self):
        print(self.cantMadera)
        if self.cantMadera >= 20:
            self.barco = True
            print("cree barco")
            self.restarMadera(20)
        else:
            self.barco = False