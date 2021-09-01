import pygame

class Celda():
    def __init__(self, terreno, naturales, construccion, propiedad, visual, num):
        self.terreno = terreno
        self.naturales = naturales
        self.construccion = construccion
        self.propiedad = propiedad
        self.visual = visual
        self.numero = num

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

    def cambiarTerreno(self, nuevoTerreno):
        self.terreno = nuevoTerreno

    def agregarNat(self, naturaleza):
        self.naturales = naturaleza
    