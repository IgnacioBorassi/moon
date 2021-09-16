from eventos import Eventos
from aire import Aire
import pygame
import sys
import random
from arbol import Arbol
from tierra import Tierra
from montana import Montana
from sprites import Sprites

class Visual:
    '''Clase que contiene todos los cambios de la pantalla'''

    def __init__(self):
        pass
    

    def cargar(self):
        '''Carga la pantalla'''

        pantalla = pygame.display.set_mode((1080,520))

        pygame.display.set_caption('Lo barato sale caro lo normal es lo raro estare sonado me visto despacio si estoy apurado amo ser odiado y tener la facha de un repetidor y la anota de un aprobado')
        fps = pygame.time.Clock()

        escalaX = 40
        escalaY = 40

        fondo_copado = pygame.Surface((1080,520))
        fondo_copado.fill((190, 190, 190))
        sprites = Sprites()

        negro_fond = sprites.getNegro_fond()
        montana_sup = sprites.getMontana_sup()
        agua_fond = sprites.getAgua_fond()
        pasto_fond = sprites.getPasto_fond()
        arbol_sup = sprites.getArbol_sup()
        pelado_sup = sprites.getPelado_sup()

        eventos = Eventos()
        inicioCeldaY = 0
        inicioCeldaX = 0
        pos_x =  0
        visualInicioY = eventos.inicioPeladoY()
        visualInicioX = eventos.inicioPeladoX()

        while (type(eventos.getTerreno(visualInicioY, visualInicioX)) != Tierra or 
        type(eventos.getNaturaleza(visualInicioY, visualInicioX)) != Aire):

            visualInicioY = eventos.inicioPeladoY()
            visualInicioX = eventos.inicioPeladoX()

        eventos.zonaInicial(visualInicioY, visualInicioX)
        eventos.cambiarVisual(visualInicioY, visualInicioX, True)
        eventos.ponerPelado(visualInicioY, visualInicioX)
        inicioCeldaY = eventos.inicioCeldaYOP(visualInicioY)
        inicioCeldaX = eventos.inicioCeldaXOP(visualInicioX)

        while True:
            eventos.repetidor(visualInicioY, visualInicioX, inicioCeldaY, inicioCeldaX)
            
            if eventos.getMenuActivo() == True:
                pantalla.blit(eventos.getFondo(),(0,0))
                pantalla.blit(eventos.getStartSup(), eventos.getStartRect())
                pantalla.blit(eventos.getExitSup(), eventos.getExitRect())
            else:

                celdasY=eventos.getCeldasY()
                celdasX = eventos.getCeldasX()
                visualInicioX = eventos.getVisualInicioX()
                visualInicioY = eventos.getVisualInicioY()
                inicioCeldaY = eventos.getInicioCeldaY()
                inicioCeldaX = eventos.getInicioCeldaX()
                pantalla.blit(fondo_copado, (0, 0))
                pos_y = inicioCeldaY

                for i in range(0, celdasY):
                    for x in range(0, celdasX):
                        if eventos.getVisual(i, x) == True:
                            if type(eventos.getTerreno(i, x)) == Tierra:
                                
                                pantalla.blit(pasto_fond, (pos_x, pos_y))
                                
                                if type(eventos.getNaturaleza(i, x)) == Arbol:
                                    pantalla.blit(arbol_sup, (pos_x, pos_y))

                                elif type(eventos.getNaturaleza(i, x)) == Montana:
                                    pantalla.blit(montana_sup, (pos_x, pos_y))

                            else:
                                pantalla.blit(agua_fond, (pos_x, pos_y))

                            if eventos.getPelado(i, x) == True:
                                pantalla.blit(pelado_sup, (pos_x, pos_y))

                        else:
                            pantalla.blit(negro_fond, (pos_x, pos_y))

                        pos_x+=escalaX
                        
                    pos_x=inicioCeldaX
                    pos_y+=escalaY

            pygame.display.update()
            fps.tick(60)
    