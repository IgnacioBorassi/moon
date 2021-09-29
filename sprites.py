import pygame

class Sprites:
    '''clase para guardar los sprites'''

    def __init__(self):
        self.escalaX = 40
        self.escalaY = 40
        self.negro_fond = None
        self.montana_sup = None
        self.agua_fond = None
        self.pasto_fond = None
        self.arbol_sup = None
        self.pelado_sup = None
        self.casa_sup = None


    def getNegro_fond(self):
        self.negro_fond = pygame.image.load('Fotuchas/negro.png').convert_alpha()
        self.negro_fond = pygame.transform.scale(self.negro_fond, (self.escalaX, self.escalaY))
        return self.negro_fond

    def getMarcador_sup(self):
        self.marcador_sup = pygame.image.load('Fotuchas/marcador_sup.png').convert_alpha()
        self.marcador_sup = pygame.transform.scale(self.marcador_sup, (self.escalaX, self.escalaY))
        return self.marcador_sup

    def getMontana_sup(self):
        self.montana_sup = pygame.image.load('Fotuchas/montana.png').convert_alpha()
        self.montana_sup = pygame.transform.scale(self.montana_sup, (self.escalaX, self.escalaY))
        return self.montana_sup



    def getAgua_fond(self):
        self.agua_fond = pygame.image.load('Fotuchas/agua.png').convert_alpha()
        self.agua_fond = pygame.transform.scale(self.agua_fond, (self.escalaX, self.escalaY))
        return self.agua_fond


    def getPasto_fond(self):
        self.pasto_fond = pygame.image.load('Fotuchas/pasto.png').convert_alpha()
        self.pasto_fond = pygame.transform.scale(self.pasto_fond, (self.escalaX, self.escalaY))
        return self.pasto_fond
    

    def getArbol_sup(self):
        self.arbol_sup = pygame.image.load('Fotuchas/arbol.png').convert_alpha()
        self.arbol_sup = pygame.transform.scale(self.arbol_sup, (self.escalaX, self.escalaY))
        return self.arbol_sup
    

    def getPelado_sup(self):
        self.pelado_sup = pygame.image.load('Fotuchas/pelado.png').convert_alpha()
        self.pelado_sup = pygame.transform.scale(self.pelado_sup, (self.escalaX, self.escalaY))
        return self.pelado_sup
    
    def getCasa_sup(self):
        self.casa_sup = pygame.image.load('Fotuchas/casa_sup.png').convert_alpha()
        self.casa_sup = pygame.transform.scale(self.casa_sup, (self.escalaX, self.escalaY))
        return self.casa_sup