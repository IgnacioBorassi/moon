from eventos import Eventos
from aire import Aire
import pygame
import sys
import random
from arbol import Arbol
from tierra import Tierra
from montana import Montana
from sprites import Sprites
from sibilisasion import civilizacion
from jugador import Jugador
import os
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
        casa_sup = sprites.getCasa_sup()
        marcador_sup = sprites.getMarcador_sup()
        piedra_sup = sprites.getPiedra_sup()
        madera_sup = sprites.getMadera_sup()
        energia_sup = sprites.getEnergia_sup()
        eventos = Eventos()
        inicioCeldaY = 0
        inicioCeldaX = 0
        pos_x =  0
        visualInicioY = eventos.inicioPeladoY()
        visualInicioX = eventos.inicioPeladoX()

        
        while True:
            if eventos.getMapa1() == True:
                eventos.cargarMapa1()
                visualInicioX = eventos.getMundoVisualX()
                print (visualInicioX)
                visualInicioY = eventos.getMundoVisualY()
                
                eventos.ponerMarcador(visualInicioY, visualInicioX, -1)
                inicioCeldaY = eventos.inicioCeldaYOP(visualInicioY)
                inicioCeldaX = eventos.inicioCeldaXOP(visualInicioX)
                
                eventos.sacarValoresMapas()

            elif eventos.getMapa2() == True:
                eventos.cargarMapa2()
                visualInicioX = eventos.getMundoVisualX()
                visualInicioY = eventos.getMundoVisualY()
                inicioCeldaY = eventos.inicioCeldaYOP(visualInicioY)
                inicioCeldaX = eventos.inicioCeldaXOP(visualInicioX)
                eventos.ponerMarcador(visualInicioY, visualInicioX, -1)
                eventos.sacarValoresMapas()
            

            elif eventos.getMapaG() == True:
                if os.stat("guardado.txt").st_size != 0:
                    eventos.cargarMapaG()
                    visualInicioX = eventos.getMundoVisualX()
                    visualInicioY = eventos.getMundoVisualY()
                    inicioCeldaY = eventos.inicioCeldaYOP(visualInicioY)
                    inicioCeldaX = eventos.inicioCeldaXOP(visualInicioX)
                    eventos.ponerMarcador(visualInicioY, visualInicioX, -1)
                    eventos.sacarValoresMapas()
                else:
                    eventos.generacionPelado(visualInicioY, visualInicioX)
                    visualInicioX = eventos.getvisualInicioX()
                    visualInicioY = eventos.getVisualInicioY()
                    
                    eventos.zonaInicial(visualInicioY, visualInicioX)
                    eventos.cambiarVisual(visualInicioY, visualInicioX, True)
                    eventos.ponerPelado(visualInicioY, visualInicioX)
                    eventos.ponerMarcador(visualInicioY, visualInicioX, -1)

                    inicioCeldaY = eventos.inicioCeldaYOP(visualInicioY)
                    inicioCeldaX = eventos.inicioCeldaXOP(visualInicioX)
                    eventos.sacarValoresMapas()

            eventos.repetidor(visualInicioY, visualInicioX, inicioCeldaY, inicioCeldaX)
            
            if eventos.getMenuActivo() == True:
                pantalla.blit(eventos.getFondo(),(0,0))
                pantalla.blit(eventos.getStartSup(), eventos.getStartRect())
                pantalla.blit(eventos.getExitSup(), eventos.getExitRect())
            
            elif eventos.getModoActivo() == True:
                pantalla.blit(eventos.getFondoModo(),(0,0))
                pantalla.blit(eventos.getBotonMapa1Sup(), eventos.getBotonMapa1Rect())
                pantalla.blit(eventos.getBotonMapa2Sup(), eventos.getBotonMapa2Rect())
                pantalla.blit(eventos.getBotonMapaGSup(), eventos.getBotonMapaGRect())
            else:

                celdasY = eventos.getCeldasY()
                celdasX = eventos.getCeldasX()
                visualInicioX = eventos.getVisualInicioX()
                visualInicioY = eventos.getVisualInicioY()
                inicioCeldaY = eventos.getInicioCeldaY()
                inicioCeldaX = eventos.getInicioCeldaX()
                pantalla.blit(fondo_copado, (0, 0))
                pos_y = inicioCeldaY
                eventos.realizarAcciones()
                
                for i in range(0, celdasY):
                    for x in range(0, celdasX):
                        if eventos.getVisual(i, x) == True:
                            if (repr(eventos.getTerreno(i, x))) == "Tierra":
                                pantalla.blit(pasto_fond, (pos_x, pos_y))
                                
                                if (repr(eventos.getNaturaleza(i, x))) == "Arbol":
                                    pantalla.blit(arbol_sup, (pos_x, pos_y))

                                elif (repr(eventos.getNaturaleza(i, x))) == "Montana":
                                    pantalla.blit(montana_sup, (pos_x, pos_y))

                            else:
                                pantalla.blit(agua_fond, (pos_x, pos_y))

                            if eventos.getPelado(i, x) == True:
                                pantalla.blit(pelado_sup, (pos_x, pos_y))
                            if eventos.getCasa(i,x) == True:
                               pantalla.blit(casa_sup, (pos_x, pos_y)) 
                        else:
                            pantalla.blit(negro_fond, (pos_x, pos_y))
                        
                        if eventos.getMarcador(i, x) == True:
                            pantalla.blit(marcador_sup, (pos_x, pos_y))
                        pos_x+=escalaX
                    
                    pantalla.blit(piedra_sup, (904, 56))
                    pantalla.blit(madera_sup, (904, 100))
                    pantalla.blit(energia_sup, (904, 21))
                    font = pygame.font.SysFont(None, 24)
                    img = font.render(eventos.getEnergia(), True, (255, 255, 0))
                    pantalla.blit(img, (950, 35))
                    img2 = font.render(eventos.getPiedra(), True, (128, 128, 128))
                    pantalla.blit(img2, (950, 70))
                    img3 = font.render(eventos.getMadera(), True, (128, 0, 0))
                    pantalla.blit(img3, (950, 110))
                    pos_x = inicioCeldaX
                    pos_y += escalaY

            pygame.display.update()
            fps.tick(60)
