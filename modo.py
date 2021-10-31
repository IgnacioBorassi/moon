import pygame

class Modo:
    def __init__(self):
        """Un menu con botones que te dejan elegir el modo de mapa(mapa1, mapa2, mapaG/random)"""
        self.activo = None
        self.boton_mapa1_sup = None
        self.boton_mapa2_sup = None
        self.boton_mapaG_sup = None
        self.boton_mapa1_rect = None
        self.boton_mapa2_rect = None
        self.boton_mapaG_rect = None
        self.fondoModo = None
        
        
    
    def cargarFondo(self):
        '''Carga el fondo'''
        self.fondoModo = pygame.Surface((1080,520))
        self.fondoModo.fill((173, 255, 47))
    
    def cargarBotones(self):
        self.boton_mapa1_sup = pygame.image.load('Fotuchas/boton_mapa1_sup.png').convert_alpha()
        self.boton_mapa1_sup = pygame.transform.scale(self.boton_mapa1_sup, (300, 195))
        self.boton_mapa1_rect = self.boton_mapa1_sup.get_rect(topleft =(50,200))

        self.boton_mapa2_sup = pygame.image.load('Fotuchas/boton_mapa2_sup.png').convert_alpha()
        self.boton_mapa2_sup = pygame.transform.scale(self.boton_mapa2_sup, (300, 195))
        self.boton_mapa2_rect = self.boton_mapa2_sup.get_rect(topleft =(400,200))

        self.boton_mapaG_sup = pygame.image.load('Fotuchas/boton_mapaG_sup.png').convert_alpha()
        self.boton_mapaG_sup = pygame.transform.scale(self.boton_mapaG_sup, (300, 195))
        self.boton_mapaG_rect = self.boton_mapaG_sup.get_rect(topleft =(750,200))
    
    def apagarModo(self):
        self.activo = False

    def activarModo(self):
        self.activo = True
        self.cargarFondo()
        self.cargarBotones()
        

    def getActivo(self):
        return self.activo
    
    def getFondoModo(self):
        return self.fondoModo
    
    def getBotonMapa1Sup(self):
        return self.boton_mapa1_sup
    
    def getBotonMapa1Rect(self):
        return self.boton_mapa1_rect
    
    def getBotonMapa2Sup(self):
        return self.boton_mapa2_sup
    
    def getBotonMapa2Rect(self):
        return self.boton_mapa2_rect
    
    def getBotonMapaGSup(self):
        return self.boton_mapaG_sup
    
    def getBotonMapaGRect(self):
        return self.boton_mapaG_rect
    
    