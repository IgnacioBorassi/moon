from sibilisasion import civilizacion

class Jugador:
    def __init__(self):
        self.energia = 500
        self.civilizacion = civilizacion()
    

    def agregarMadera(self, cant):
        self.civilizacion.agregarMadera(cant)

    def restarEnergia(self, cant):
        self.energia -= cant
    
    def crearBarco(self):
        self.civilizacion.CrearBarco()