import pygame

class Marcador:
    '''Proximamente en algun dia'''
    
    def __init__(self, marcador):
        self.marcador = marcador
    
    def cambiarMarcador(self, marcador):
        self.marcador = marcador 
        
    def ponerMarcador(self):
        self.cambiarMarcador(True)

    def sacarMarcador(self):
        self.cambiarMarcador(False)

    def getMarcador(self):
        return self.marcador