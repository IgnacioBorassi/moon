from pygame import event, sprite
from eventos import Eventos
from aire import Aire
import pygame
import sys
import random
from arbol import Arbol
from fundador import Fundador
from mina import Mina
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
        barco_sup = sprites.getBarco_sup()
        guerrero_sup = sprites.getGuerrero_sup()
        arquero_sup = sprites.getArquero_sup()
        obrero_sup = sprites.getObrero_sup()
        puerto_sup = sprites.getPuerto_sup()
        mina_sup = sprites.getMina_sup()
        pez_sup = sprites.getPez_sup()
        bordeArriba_sup = sprites.getBordeArriba_sup()
        bordeAbajo_sup = sprites.getBordeAbajo_sup()
        bordeIzquierda_sup = sprites.getBordeIzquierda_sup()
        bordeIzquierdaAbajo_sup = sprites.getBordeIzquierdaAbajo_sup()
        bordeIzquierdaArriba_sup = sprites.getBordeIzquierdaArriba_sup()
        bordeDerecha_sup = sprites.getBordeDerecha_sup()
        bordeDerechaAbajo_sup = sprites.getBordeDerechaAbajo_sup()
        bordeDerechaArriba_sup = sprites.getBordeDerechaArriba_sup()
        pel_bordeArriba_sup = sprites.getpel_BordeArriba_sup()
        pel_bordeAbajo_sup = sprites.getpel_BordeAbajo_sup()
        pel_bordeIzquierda_sup = sprites.getpel_BordeIzquierda_sup()
        pel_bordeIzquierdaAbajo_sup = sprites.getpel_BordeIzquierdaAbajo_sup()
        pel_bordeIzquierdaArriba_sup = sprites.getpel_BordeIzquierdaArriba_sup()
        pel_bordeDerecha_sup = sprites.getpel_BordeDerecha_sup()
        pel_bordeDerechaAbajo_sup = sprites.getpel_BordeDerechaAbajo_sup()
        pel_bordeDerechaArriba_sup = sprites.getpel_BordeDerechaArriba_sup()
        corral_sup = sprites.getCorral_sup()
        cultivo_sup = sprites.getCultivo_sup()
        peludo_sup = sprites.getPeludo_sup()
        peludocasa_sup = sprites.getPeludoCasa_sup()

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
                    eventos.zonaInicialPeludo()
                    eventos.cambiarVisual(visualInicioY, visualInicioX, True)
                    eventos.ponerPelado(visualInicioY, visualInicioX, Fundador())
                    eventos.ponerMarcador(visualInicioY, visualInicioX, -1)

                    inicioCeldaY = eventos.inicioCeldaYOP(visualInicioY)
                    inicioCeldaX = eventos.inicioCeldaXOP(visualInicioX)
                    eventos.sacarValoresMapas()

            if eventos.getCantTurno() == 200:
                eventos.activarFinal()
                eventos.repetidor(visualInicioY, visualInicioX, inicioCeldaY, inicioCeldaX)
                if eventos.getActivoFinal() == True:
                    pantalla.blit(eventos.getFondoFinal(),(0,0))
                    pantalla.blit(eventos.getReiniciarsup(), eventos.getReiniciarRect())
                    pantalla.blit(eventos.getCerrarSup(), eventos.getCerrarRect())
            else:
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
                                        if eventos.getMina(i,x) == True:
                                            pantalla.blit(mina_sup, (pos_x, pos_y))

                                else:
                                    pantalla.blit(agua_fond, (pos_x, pos_y))
                            
                                if eventos.getCorral(i,x) == True:
                                    pantalla.blit(corral_sup, (pos_x, pos_y)) 
                        
                                if eventos.getCultivo(i,x) == True:
                                    pantalla.blit(cultivo_sup, (pos_x, pos_y)) 

                                if eventos.getCasa(i,x) == True:
                                    pantalla.blit(casa_sup, (pos_x, pos_y))

                                if eventos.getPeludoCasa(i, x) == True:
                                    pantalla.blit(peludocasa_sup, (pos_x, pos_y))
                                    
                                if eventos.getPelado(i, x) == True:
                                    if (repr(eventos.getTerreno(i, x))) == "Tierra":
                                        
                                        if (repr(eventos.getClase(i, x))) == "Guerrero":
                                            
                                            pantalla.blit(guerrero_sup, (pos_x, pos_y))

                                        elif (repr(eventos.getClase(i, x))) == "Arquero":
                                            
                                            pantalla.blit(arquero_sup, (pos_x, pos_y))
                                        
                                        elif (repr(eventos.getClase(i, x))) == "Obrero":
                                            
                                            pantalla.blit(obrero_sup, (pos_x, pos_y))

                                        elif (repr(eventos.getClase(i, x))) == "Peludo":
                                            
                                            pantalla.blit(peludo_sup, (pos_x, pos_y))

                                        else:
                                            pantalla.blit(pelado_sup, (pos_x, pos_y))

                                    else:
                                        pantalla.blit(barco_sup,(pos_x, pos_y))
                                

                                if eventos.getPuerto(i,x) == True:
                                    pantalla.blit(puerto_sup, (pos_x, pos_y))

                                borde = eventos.bordeVisual(i, x)
                                if borde == "borde_arriba_derecha":
                                    pantalla.blit(bordeDerechaArriba_sup, (pos_x, pos_y))
                                elif borde == "borde_arriba_izquierda":
                                    pantalla.blit(bordeIzquierdaArriba_sup, (pos_x, pos_y))
                                elif borde == "borde_abajo_izquierda":
                                    pantalla.blit(bordeIzquierdaAbajo_sup, (pos_x, pos_y))
                                elif borde == "borde_abajo_derecha":
                                    pantalla.blit(bordeDerechaAbajo_sup, (pos_x, pos_y))
                                elif borde == "borde_derecha":
                                    pantalla.blit(bordeDerecha_sup, (pos_x, pos_y))
                                elif borde == "borde_izquierda":
                                    pantalla.blit(bordeIzquierda_sup, (pos_x, pos_y))
                                elif borde == "borde_arriba":
                                    pantalla.blit(bordeArriba_sup, (pos_x, pos_y))
                                elif borde == "borde_abajo":
                                    pantalla.blit(bordeAbajo_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_arriba_derecha":
                                    pantalla.blit(pel_bordeDerechaArriba_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_arriba_izquierda":
                                    pantalla.blit(pel_bordeIzquierdaArriba_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_abajo_izquierda":
                                    pantalla.blit(pel_bordeIzquierdaAbajo_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_abajo_derecha":
                                    pantalla.blit(pel_bordeDerechaAbajo_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_derecha":
                                    pantalla.blit(pel_bordeDerecha_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_izquierda":
                                    pantalla.blit(pel_bordeIzquierda_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_arriba":
                                    pantalla.blit(pel_bordeArriba_sup, (pos_x, pos_y))
                                elif borde == "pel_borde_abajo":
                                    pantalla.blit(pel_bordeAbajo_sup, (pos_x, pos_y))
                            

                            else:
                                pantalla.blit(negro_fond, (pos_x, pos_y))
                            
                            if eventos.getMarcador(i, x) == True:
                                pantalla.blit(marcador_sup, (pos_x, pos_y))
                            pos_x+=escalaX
                        
                        pantalla.blit(piedra_sup, (904, 56))
                        pantalla.blit(madera_sup, (904, 100))
                        pantalla.blit(energia_sup, (904, 21))
                        pantalla.blit(pez_sup, (904, 150))

                        font = pygame.font.SysFont(None, 24)
                        img = font.render(eventos.getEnergia(), True, (255, 255, 0))
                        pantalla.blit(img, (950, 35))
                        img2 = font.render(eventos.getPiedra(), True, (128, 128, 128))
                        pantalla.blit(img2, (950, 70))
                        img3 = font.render(eventos.getMadera(), True, (128, 0, 0))
                        pantalla.blit(img3, (950, 110))
                        img4 = font.render(eventos.getComida(), True, (128, 128, 128))
                        pantalla.blit(img4, (950, 160))

                        if eventos.getBarco()== True:
                            pantalla.blit(barco_sup, (904, 190))
                            img4 = font.render(eventos.getUsoBarco(), True, (128, 0, 0))
                            pantalla.blit(img4, (950, 200))
                        else:
                            pantalla.blit(negro_fond, (pos_x, pos_y))
                        if eventos.getMarcador(i, x) == True:
                            pantalla.blit(marcador_sup, (pos_x, pos_y))
                        pos_x += escalaX
                    
                        pos_x = inicioCeldaX
                        pos_y += escalaY

            pygame.display.update()
            fps.tick(60)
