import pygame

class Menu:
    '''Un menu con boton de salir y boton start'''

    def __init__(self):
        self.activo = True
        self.boton_start_sup = None
        self.boton_exit_sup = None
        self.fondo_menu = None
        self.boton_start_rect = None
        self.boton_exit_rect = None
        self.cargarFondo()
        self.cargarBotones()


    def apagarMenu(self):
        self.activo = False

    def prenderMenu(self):
        self.activo = True

    def getActivo(self):
        return self.activo

    def getFondo(self):
        return self.fondo_menu

    def cargarFondo(self):
        '''Carga el fondo'''
        self.fondo_menu = pygame.Surface((1080,520))
        self.fondo_menu.fill((173, 255, 47))
    

    def cargarBotones(self):
        '''Carga los botones'''
        self.boton_start_sup = pygame.image.load('Fotuchas/pelado_start.png').convert_alpha()
        self.boton_start_sup = pygame.transform.scale(self.boton_start_sup, (300, 195))
        self.boton_start_rect = self.boton_start_sup.get_rect(topleft =(100,200))

        self.boton_exit_sup = pygame.image.load('Fotuchas/boton_exit.png').convert_alpha()
        self.boton_exit_sup = pygame.transform.scale(self.boton_exit_sup, (300, 195))
        self.boton_exit_rect = self.boton_exit_sup.get_rect(topleft =(600, 200))

    def getStartSup(self):
        return self.boton_start_sup
    
    def getExitSup(self):
        return self.boton_exit_sup
    
    def getStartRect(self):
        return self.boton_start_rect
    
    def getExitRect(self):
        return self.boton_exit_rect