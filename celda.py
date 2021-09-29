import pygame
from persona import Persona
from marcador import Marcador
from casa import Casa

class Celda():
    '''Clase Celda contiene el terreno, el propietario, visual y un numero'''

    def __init__(self, terreno, propiedad, visual, num):
        self.terreno = terreno
        self.propiedad = propiedad
        self.visual = visual
        self.numero = num
        self.persona = Persona(None)
        self.marca = Marcador(None)
        self.casa = Casa(None)

    def tomarTerreno(self, propiedad):
        self.propiedad = propiedad
    
    def visualizar(self, visual):
        '''Permite ver o no ver la celda'''
        self.visual = visual

    def getTerreno(self):
        return self.terreno

    def getNum(self):
        return self.numero
        
    def getMarcador(self):
        return self.marcador.getMarcador()
    
    def getConstruccion(self):
        self.terreno.getConstruccion()

    def ponerMarcador(self):
        self.marcador.ponerMarcador()

    def sacarMarcador(self):
        self.marcador.sacarMarcador()

    def cambiarTerreno(self, nuevoTerreno):
        '''Cambia el terreno entre tierra y agua'''
        self.terreno = nuevoTerreno

    def cambiarNaturaleza(self, nuevaNaturaleza):
        '''Cambia la celda entre arbol y montana'''
        self.terreno.cambiarNaturaleza(nuevaNaturaleza)  
    
    def getNaturaleza(self):
        return self.terreno.getNaturaleza()

    def getVisual(self):
        return self.visual
    
    def cambiarVisual(self, nuevoVisual):
        '''Cambia la celda para poder visualizarla'''
        self.visual = nuevoVisual

    def ponerPelado(self):
        self.persona.ponerPelado()

    def sacarPelado(self):
        self.persona.sacarPelado()

    def getPelado(self):
        return self.persona.getPersona()

    def ponerCasa(self):
        self.casa.ponerCasa()
    
    def getCasa(self):
        return self.casa.getCasa()