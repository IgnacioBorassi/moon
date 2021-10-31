import pygame

class Marcador:
    '''Representa el marcador que posee un orden'''
    
    def __init__(self, marcador):
        self.marcador = marcador
        self.orden = -1
    
    def cambiarMarcador(self, marcador):
        self.marcador = marcador 
    
    def cambiarOrden(self, nuevoOrden):
        self.orden = nuevoOrden

    def ponerMarcador(self, nuevoOrden):
        self.cambiarMarcador(True)
        self.cambiarOrden(nuevoOrden)

    def sacarMarcador(self):
        self.cambiarMarcador(False)
        self.cambiarOrden(-1)

    def getMarcador(self):
        return self.marcador
    
    def getOrdenMarcador(self):
        return self.orden