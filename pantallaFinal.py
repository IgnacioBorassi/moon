import pygame
import os

class PantallaFinal:
    def __init__(self):
        self.activo = None
        self.fondo_Final = None
        self.boton_Reiniciar_rect = None
        self.boton_Cerrar_rect = None
        self.boton_Reiniciar_sup = None
        self.boton_Cerrar_sup = None
    
    def apagarFinal(self):
        self.activo = False
    
    def prender(self):
        self.activo = True
        self.cargarFondo()
        self.cargarBotones()

    def getActivo(self):
        return self.activo

    def getFondo(self):
        return self.fondo_Final

    def cargarFondo(self):
        '''Carga el fondo'''
        self.fondo_Final = pygame.Surface((1080,520))
        self.fondo_Final.fill((173, 255, 47))
    

    def cargarBotones(self):
        '''Carga los botones'''
        self.boton_Reiniciar_sup = pygame.image.load('Fotuchas/pelado_start.png').convert_alpha()
        self.boton_Reiniciar_sup = pygame.transform.scale(self.boton_Reiniciar_sup, (300, 195))
        self.boton_Reiniciar_rect = self.boton_Reiniciar_sup.get_rect(topleft =(100,200))

        self.boton_Cerrar_sup= pygame.image.load('Fotuchas/boton_exit.png').convert_alpha()
        self.boton_Cerrar_sup = pygame.transform.scale(self.boton_Cerrar_sup, (300, 195))
        self.boton_Cerrar_rect = self.boton_Cerrar_sup.get_rect(topleft =(600, 200))
    
    def getReiniciarsup(self):
        return self.boton_Reiniciar_sup
    
    def getCerrarSup(self):
        return self.boton_Cerrar_sup
    
    def getReiniciarRect(self):
        return self.boton_Reiniciar_rect
    
    def getCerrarRect(self):
        return self.boton_Cerrar_rect
    

