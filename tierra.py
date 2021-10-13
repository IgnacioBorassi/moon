from aire import Aire
from arbol import Arbol

class Tierra:
    '''Representa la tierra y su construccion'''
    
    def __init__(self, naturaleza, construccion):
        self.naturaleza = naturaleza
        self.construccion = construccion


    def getNaturaleza(self):
        return self.naturaleza
    
    def getConstruccion(self):
        return self.construccion
    
    def cambiarNaturaleza(self, naturaleza):
        '''Cambia naturaleza entre montana, arbol y aire'''
        self.naturaleza = naturaleza

    def sacarArbol(self):
        self.cambiarNaturaleza(Aire())
    
    def randomMaterial(self):
        return self.naturaleza.randomMaterial()
    
    def __repr__(self) -> str:
        return "Tierra"