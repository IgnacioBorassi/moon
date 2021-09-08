import pygame
class Marcador:
    def __init__(self, marcar):
        self.marcar = marcar
    
    def cambiarMarcador(self, marcador):
        self.marcador = marcador 
        
    def ponerMarcador(self):
        self.cambiarMarcador(True)

    def sacarMarcador(self):
        self.cambiarMarcador(False)

    def getMarcador(self):
        return self.marcar