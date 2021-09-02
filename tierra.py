class Tierra:
    def __init__(self, naturaleza, construccion):
        self.naturaleza = naturaleza
        self.construccion = construccion

    def getNaturaleza(self):
        return self.naturaleza
    
    def getConstruccion(self):
        return self.construccion
    
    def cambiarNaturaleza(self, naturaleza):
        self.naturaleza = naturaleza