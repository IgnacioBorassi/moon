from guerrero import Guerrero
from arquero import Arquero
from obrero import Obrero

class Persona:
    '''Una persona que en realidad es un pelado'''
    
    def __init__(self, persona):
        self.persona = persona
        self.clase = None


    def cambiarPelado(self, persona):
        '''Cambia el atributo persona'''
        self.persona = persona
    

    def ponerPelado(self, nuevaClase):
        self.cambiarPelado(True)
        self.cambiarClase(nuevaClase)

    def sacarPelado(self):
        self.cambiarPelado(False)
        self.clase = None
    
    def cambiarClase(self, nuevaClase):
        self.clase = nuevaClase
        

    def getPersona(self):
        return self.persona
    
    def getClase(self):
        return self.clase
    
    def __repr__(self) -> str:
        return "Persona"