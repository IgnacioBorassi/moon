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
        self.piedra_sup = None
        self.madera_sup = None
        self.energia_sup = None
        self.barco_sup = None
        self.guerrrero_sup = None
        self.obrero_sup = None
        self.arquero_sup = None
        self.puerto_sup = None
        self.pez_sup = None
        self.corral_sup = None
        self.cultivo_sup = None


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

    def getPiedra_sup(self):
        self.piedra_sup = pygame.image.load('Fotuchas/piedra.png').convert_alpha()
        self.piedra_sup = pygame.transform.scale(self.piedra_sup, (self.escalaX, self.escalaY))
        return self.piedra_sup

    def getMadera_sup(self):
        self.madera_sup = pygame.image.load('Fotuchas/madera.png').convert_alpha()
        self.madera_sup = pygame.transform.scale(self.madera_sup, (self.escalaX, self.escalaY))
        return self.madera_sup
    
    def getEnergia_sup(self):
        self.energia_sup = pygame.image.load('Fotuchas/energia.png').convert_alpha()
        self.energia_sup = pygame.transform.scale(self.energia_sup, (self.escalaX, self.escalaY))
        return self.energia_sup

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
        self.pelado_sup = pygame.image.load('Fotuchas/pelado_sup.png').convert_alpha()
        self.pelado_sup = pygame.transform.scale(self.pelado_sup, (self.escalaX, self.escalaY))
        return self.pelado_sup
    
    def getPeludo_sup(self):
        self.peludo_sup = pygame.image.load('Fotuchas/peludo_sup.png').convert_alpha()
        self.peludo_sup = pygame.transform.scale(self.peludo_sup, (self.escalaX, self.escalaY))
        return self.peludo_sup

    def getCasa_sup(self):
        self.casa_sup = pygame.image.load('Fotuchas/casa_sup.png').convert_alpha()
        self.casa_sup = pygame.transform.scale(self.casa_sup, (self.escalaX, self.escalaY))
        return self.casa_sup

    def getPeludoCasa_sup(self):
        self.peludoCasa_sup = pygame.image.load('Fotuchas/peludocasa.png').convert_alpha()
        self.peludoCasa_sup = pygame.transform.scale(self.peludoCasa_sup, (self.escalaX, self.escalaY))
        return self.peludoCasa_sup
    
    def getBarco_sup(self):
        self.barco_sup = pygame.image.load('Fotuchas/barco_sup.png').convert_alpha()
        self.barco_sup = pygame.transform.scale(self.barco_sup, (self.escalaX, self.escalaY))
        return self.barco_sup
    
    def getGuerrero_sup(self):
        self.guerrero_sup = pygame.image.load('Fotuchas/peladoGuerrero_sup.png').convert_alpha()
        self.guerrero_sup = pygame.transform.scale(self.guerrero_sup, (self.escalaX, self.escalaY))
        return self.guerrero_sup
    
    def getArquero_sup(self):
        self.arquero_sup = pygame.image.load('Fotuchas/peladoArquero_sup.png').convert_alpha()
        self.arquero_sup = pygame.transform.scale(self.arquero_sup, (self.escalaX, self.escalaY))
        return self.arquero_sup
    
    def getObrero_sup(self):
        self.obrero_sup = pygame.image.load('Fotuchas/peladoObrero_sup.png').convert_alpha()
        self.obrero_sup = pygame.transform.scale(self.obrero_sup, (self.escalaX, self.escalaY))
        return self.obrero_sup

    def getPuerto_sup(self):
        self.puerto_sup = pygame.image.load('Fotuchas/Puerto_sup.png').convert_alpha()
        self.puerto_sup = pygame.transform.scale(self.puerto_sup, (self.escalaX, self.escalaY))
        return self.puerto_sup
    
    def getMina_sup(self):
        self.mina_sup = pygame.image.load('Fotuchas/Mina_sup.png').convert_alpha()
        self.mina_sup = pygame.transform.scale(self.mina_sup, (self.escalaX, self.escalaY))
        return self.mina_sup

    def getPez_sup(self):
        self.pez_sup = pygame.image.load('Fotuchas/Pez_sup.png').convert_alpha()
        self.pez_sup = pygame.transform.scale(self.pez_sup, (self.escalaX, self.escalaY))
        return self.pez_sup

    def getBordeArriba_sup(self):
        self.bordeArriba_sup = pygame.image.load('Fotuchas/borde_arriba.png').convert_alpha()
        self.bordeArriba_sup = pygame.transform.scale(self.bordeArriba_sup, (self.escalaX, self.escalaY))
        return self.bordeArriba_sup
    
    def getBordeAbajo_sup(self):
        self.bordeAbajo_sup = pygame.image.load('Fotuchas/borde_abajo.png').convert_alpha()
        self.bordeAbajo_sup = pygame.transform.scale(self.bordeAbajo_sup, (self.escalaX, self.escalaY))
        return self.bordeAbajo_sup

    def getBordeDerecha_sup(self):
        self.bordeDerecha_sup = pygame.image.load('Fotuchas/borde_derecha.png').convert_alpha()
        self.bordeDerecha_sup = pygame.transform.scale(self.bordeDerecha_sup, (self.escalaX, self.escalaY))
        return self.bordeDerecha_sup
    
    def getBordeIzquierda_sup(self):
        self.bordeIzquierda_sup = pygame.image.load('Fotuchas/borde_izquierda.png').convert_alpha()
        self.bordeIzquierda_sup = pygame.transform.scale(self.bordeIzquierda_sup, (self.escalaX, self.escalaY))
        return self.bordeIzquierda_sup

    def getBordeIzquierdaArriba_sup(self):
        self.bordeIzquierdaArriba_sup = pygame.image.load('Fotuchas/borde_izquierda_arriba.png').convert_alpha()
        self.bordeIzquierdaArriba_sup = pygame.transform.scale(self.bordeIzquierdaArriba_sup, (self.escalaX, self.escalaY))
        return self.bordeIzquierdaArriba_sup

    def getBordeIzquierdaAbajo_sup(self):
        self.bordeIzquierdaAbajo_sup = pygame.image.load('Fotuchas/borde_izquierda_abajo.png').convert_alpha()
        self.bordeIzquierdaAbajo_sup = pygame.transform.scale(self.bordeIzquierdaAbajo_sup, (self.escalaX, self.escalaY))
        return self.bordeIzquierdaAbajo_sup

    def getBordeDerechaArriba_sup(self):
        self.bordeDerechaArriba_sup = pygame.image.load('Fotuchas/borde_derecha_arriba.png').convert_alpha()
        self.bordeDerechaArriba_sup = pygame.transform.scale(self.bordeDerechaArriba_sup, (self.escalaX, self.escalaY))
        return self.bordeDerechaArriba_sup

    def getBordeDerechaAbajo_sup(self):
        self.bordeDerechaAbajo_sup = pygame.image.load('Fotuchas/borde_derecha_abajo.png').convert_alpha()
        self.bordeDerechaAbajo_sup = pygame.transform.scale(self.bordeDerechaAbajo_sup, (self.escalaX, self.escalaY))
        return self.bordeDerechaAbajo_sup

    def getpel_BordeArriba_sup(self):
        self.pel_bordeArriba_sup = pygame.image.load('Fotuchas/pel_borde_arriba.png').convert_alpha()
        self.pel_bordeArriba_sup = pygame.transform.scale(self.pel_bordeArriba_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeArriba_sup
    
    def getpel_BordeAbajo_sup(self):
        self.pel_bordeAbajo_sup = pygame.image.load('Fotuchas/pel_borde_abajo.png').convert_alpha()
        self.pel_bordeAbajo_sup = pygame.transform.scale(self.pel_bordeAbajo_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeAbajo_sup

    def getpel_BordeDerecha_sup(self):
        self.pel_bordeDerecha_sup = pygame.image.load('Fotuchas/pel_borde_derecha.png').convert_alpha()
        self.pel_bordeDerecha_sup = pygame.transform.scale(self.pel_bordeDerecha_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeDerecha_sup
    
    def getpel_BordeIzquierda_sup(self):
        self.pel_bordeIzquierda_sup = pygame.image.load('Fotuchas/pel_borde_izquierda.png').convert_alpha()
        self.pel_bordeIzquierda_sup = pygame.transform.scale(self.pel_bordeIzquierda_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeIzquierda_sup

    def getpel_BordeIzquierdaArriba_sup(self):
        self.pel_bordeIzquierdaArriba_sup = pygame.image.load('Fotuchas/pel_borde_izquierda_arriba.png').convert_alpha()
        self.pel_bordeIzquierdaArriba_sup = pygame.transform.scale(self.pel_bordeIzquierdaArriba_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeIzquierdaArriba_sup

    def getpel_BordeIzquierdaAbajo_sup(self):
        self.pel_bordeIzquierdaAbajo_sup = pygame.image.load('Fotuchas/pel_borde_izquierda_abajo.png').convert_alpha()
        self.pel_bordeIzquierdaAbajo_sup = pygame.transform.scale(self.pel_bordeIzquierdaAbajo_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeIzquierdaAbajo_sup

    def getpel_BordeDerechaArriba_sup(self):
        self.pel_bordeDerechaArriba_sup = pygame.image.load('Fotuchas/pel_borde_derecha_arriba.png').convert_alpha()
        self.pel_bordeDerechaArriba_sup = pygame.transform.scale(self.pel_bordeDerechaArriba_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeDerechaArriba_sup

    def getpel_BordeDerechaAbajo_sup(self):
        self.pel_bordeDerechaAbajo_sup = pygame.image.load('Fotuchas/pel_borde_derecha_abajo.png').convert_alpha()
        self.pel_bordeDerechaAbajo_sup = pygame.transform.scale(self.pel_bordeDerechaAbajo_sup, (self.escalaX, self.escalaY))
        return self.pel_bordeDerechaAbajo_sup

    def getCorral_sup(self):
        self.corral_sup = pygame.image.load('Fotuchas/corral_sup.png').convert_alpha()
        self.corral_sup = pygame.transform.scale(self.corral_sup, (self.escalaX, self.escalaY))
        return self.corral_sup
    
    def getCultivo_sup(self):
        self.cultivo_sup = pygame.image.load('Fotuchas/cultivo_sup.png').convert_alpha()
        self.cultivo_sup = pygame.transform.scale(self.cultivo_sup, (self.escalaX, self.escalaY))
        return self.cultivo_sup