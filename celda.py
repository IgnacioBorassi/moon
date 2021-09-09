import pygame
from persona import Persona

from marcador import Marcador
class Celda():
    def __init__(self, terreno, propiedad, visual, num):
        self.terreno = terreno
        self.propiedad = propiedad
        self.visual = visual
        self.numero = num
        self.persona = Persona(None)
        self.marca = Marcador(None)

    def construir(self, construccion):
        '''Permite construir algo en la celda'''
        self.construccion = construccion
    
    def tomarTerreno(self, propiedad):
        '''Permite apropiarse de la celda'''
        self.propiedad = propiedad
    
    def visualizar(self, visual):
        '''Permite ver la celda'''
        self.visual = visual

    def getTerreno(self):
        return self.terreno

    def getNum(self):
        return self.numero
        
    def getMarcador(self):
        return self.marcador.getMarcador()
    
    def ponerMarcador(self):
        self.marcador.ponerMarcador()

    def sacarMarcador(self):
        self.marcador.sacarMarcador()

    def cambiarTerreno(self, nuevoTerreno):
        self.terreno = nuevoTerreno

    def cambiarNaturaleza(self, nuevaNaturaleza):
        self.terreno.cambiarNaturaleza(nuevaNaturaleza)  
    
    def getNaturaleza(self):
        return self.terreno.getNaturaleza()

    def getVisual(self):
        return self.visual
    
    def cambiarVisual(self, nuevoVisual):
        self.visual = nuevoVisual

    def ponerPelado(self):
        self.persona.ponerPelado()

    def sacarPelado(self):
        self.persona.sacarPelado()

    def getPelado(self):
        return self.persona.getPersona()