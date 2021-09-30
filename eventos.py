from aire import Aire
import pygame, sys, random
from mundo import Mundo
from arbol import Arbol
from tierra import Tierra
from montana import Montana
from menu import Menu


class Eventos:
    '''Controlador de eventos'''
    
    def __init__(self):
        self.pantallaX = 1080
        self.pantallaY = 520
        self.celdasX = 216
        self.celdasY = 104
        self.visualInicioY = None
        self.visualInicioX = None
        self.menu = Menu()
        self.mundo = Mundo(self.celdasX, self.celdasY)
        self.escalaX = 40
        self.escalaY = 40
        self.seleccion = False


    def inicioCeldaYOP(self, y):
        '''Calculo para centrar la pantalla'''
        return (y * - self.escalaY) + self.escalaY * int((self.pantallaY/self.escalaY)/2)


    def inicioCeldaXOP(self, x):
        '''Calculo para centrar la pantalla'''
        return (x * - self.escalaX) + self.escalaX * int((self.pantallaX/self.escalaX)/2)


    def getInicioCeldaX(self):
        return self.inicioCeldaX

    def getInicioCeldaY(self):
        return self.inicioCeldaY

    def getVisualInicioY(self):
        return self.visualInicioY

    def getVisualInicioX(self):
        return self.visualInicioX

    def getCasa(self, y, x):
        return self.mundo.getCasa(y, x)


    def repetidor(self, visualInicioY, visualInicioX, inicioCeldaY, inicioCeldaX):
        '''Realiza los eventos relacionados con el teclado y mouse'''

        self.visualInicioY = visualInicioY
        self.visualInicioX = visualInicioX  
        self.inicioCeldaX = inicioCeldaX
        self.inicioCeldaY = inicioCeldaY

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu.getStartRect().collidepoint(event.pos):
                    self.menu.apagarMenu()
                elif self.menu.getExitRect().collidepoint(event.pos):
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu.prenderMenu()

                if self.menu.getActivo() == False:
                    if event.key == pygame.K_1:
                        #for i in range(0, self.celdasY):
                            #for x in range(0, self.celdasX):
                                if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                                and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Aire):
                                    self.mundo.ponerCasa(self.visualInicioY, self.visualInicioX)

                                if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                                and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Arbol): 
                                    print (self.mundo.cantidadMaterial(self.visualInicioY, self.visualInicioX))
                                    self.mundo.sacarArbol(self.visualInicioY, self.visualInicioX)

                                if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                                and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Montana):
                                    print (self.mundo.cantidadMaterial(self.visualInicioY, self.visualInicioX))
                    if event.key == pygame.K_j:
                        self.inicioCeldaY = ((self.visualInicioY * - self.escalaY) +
                            self.escalaY * int((self.pantallaY/self.escalaY)/2))

                        self.inicioCeldaX = ((self.visualInicioX * - self.escalaX) +
                            self.escalaX * int((self.pantallaX/self.escalaX)/2))



                    '''if event.key == pygame.K_w:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioY -= 1

                        if self.visualInicioY < 1:
                            self.visualInicioY = 1

                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                        and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Aire):

                            self.mundo.cambiarVisualY(self.visualInicioY, self.visualInicioX, (-1))
                            
                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))

                        else:
                            self.visualInicioY += 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                    if event.key == pygame.K_a:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioX -= 1
                        if self.visualInicioX < 1:
                            self.visualInicioX = 1
                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra and 
                        type(self.mundo.getNaturaleza(self.visualInicioY,self.visualInicioX)) == Aire):
                            
                            self.mundo.cambiarVisualX(self.visualInicioY, self.visualInicioX, (-1))

                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))

                        else: 
                            self.visualInicioX += 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                    if event.key == pygame.K_s:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioY += 1
                        if self.visualInicioY > (self.celdasY - 3):
                            self.visualInicioY = (self.celdasY - 3)

                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                        and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Aire):

                            self.mundo.cambiarVisualY(self.visualInicioY, self.visualInicioX, (1))

                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))

                        else:
                            self.visualInicioY -= 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                    if event.key == pygame.K_d:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioX += 1

                        if self.visualInicioX > (self.celdasX - 3):
                            self.visualInicioX = (self.celdasX - 3)

                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                        and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Aire):

                            self.mundo.cambiarVisualX(self.visualInicioY, self.visualInicioX, (1))
                            
                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))

                        else:
                            self.visualInicioX -= 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                    '''
                    
                    if event.key == pygame.K_SPACE:
                        if self.seleccion == True:
                            self.seleccion = False
                        else:
                            self.seleccion = True

                    if event.key == pygame.K_w:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                        self.visualInicioY -= 1

                        if self.visualInicioY < 1:
                            self.visualInicioY = 1
                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX)   
                    if event.key == pygame.K_a:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                        self.visualInicioX -= 1
                        if self.visualInicioX < 1:
                            self.visualInicioX = 1
                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX)
                    if event.key == pygame.K_s:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                        self.visualInicioY += 1
                        if self.visualInicioY > (self.celdasY - 3):
                            self.visualInicioY = (self.celdasY - 3)
                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX)
                    if event.key == pygame.K_d:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                        self.visualInicioX += 1

                        if self.visualInicioX > (self.celdasX - 3):
                            self.visualInicioX = (self.celdasX - 3)
                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX)
                    

                    if event.key == pygame.K_DOWN:
                        self.inicioCeldaY -= self.escalaY
                        limiteAbajoY = ((self.celdasY * self.escalaY - 
                        self.escalaY * int(self.pantallaY/self.escalaY)) * -1)
                        
                        if self.inicioCeldaY < limiteAbajoY:
                            self.inicioCeldaY = limiteAbajoY
                    
                        print("Eje Y Lista: " + str(self.inicioCeldaY))
                        print("Eje X Lista: " + str(self.inicioCeldaX))
                  
                    if event.key == pygame.K_UP:
                        self.inicioCeldaY += self.escalaY

                        if self.inicioCeldaY > 0:
                            self.inicioCeldaY = 0
                        
                        print("Eje Y Lista: " + str(self.inicioCeldaY))
                        print("Eje X Lista: " + str(self.inicioCeldaX))
                    
                    if event.key == pygame.K_RIGHT:
                        self.inicioCeldaX -= self.escalaX
                        limiteDerechaX = ((self.celdasX * self.escalaX - 
                        self.escalaX * int(self.pantallaX/self.escalaX)) * -1)
                        if self.inicioCeldaX < limiteDerechaX:
                            self.inicioCeldaX = limiteDerechaX
                        
                        print("Eje Y Lista: " + str(self.inicioCeldaY))
                        print("Eje X Lista: " + str(self.inicioCeldaX))

                    if event.key == pygame.K_LEFT:
                        self.inicioCeldaX += self.escalaX
                        if self.inicioCeldaX > 0:
                            self.inicioCeldaX = 0

                        print("Eje Y Lista: " + str(self.inicioCeldaY))
                        print("Eje X Lista: " + str(self.inicioCeldaX))

                    
    
    def getCeldasX(self):
        return self.celdasX

    def getCeldasY(self):
        return self.celdasY

    def getMenuActivo(self):
        return self.menu.getActivo()

    def inicioPeladoY(self):
        y = int(random.randrange(20,80))
        return y
    
    def inicioPeladoX(self):
        x = int(random.randrange(20,190))
        return x
    
    def zonaInicial(self, y, x):
        self.mundo.zonaInicial(y, x)

    def cambiarVisual(self, y, x, nuevoVisual):
        self.mundo.cambiarVisual(y, x, nuevoVisual)

    def ponerPelado(self, y, x):
        self.mundo.ponerPelado(y, x)
    
    def ponerMarcador(self, y, x):
        self.mundo.ponerMarcador(y, x)

    def getVisual(self, y, x):
        return self.mundo.getVisual(y, x)
    
    def getTerreno(self, y, x):
        return self.mundo.getTerreno(y, x)

    def getNaturaleza(self, y, x):
        return self.mundo.getNaturaleza(y, x)
    
    def getPelado(self, y, x):
        return self.mundo.getPelado(y, x)

    def getMarcador(self, y, x):
        return self.mundo.getMarcador(y, x)

    def getFondo(self):
        return self.menu.getFondo()
    
    def getStartSup(self):
        return self.menu.getStartSup()
    
    def getStartRect(self):
        return self.menu.getStartRect()
    
    def getExitSup(self):
        return self.menu.getExitSup()

    def getExitRect(self):
        return self.menu.getExitRect()
    
    def getCasa(self, y, x):
        return self.mundo.getCasa(y, x)
    
    def generacionPelado(self, visualInicioY, visualInicioX):
        while (type(self.getTerreno(visualInicioY, visualInicioX)) != Tierra or 
            type(self.getNaturaleza(visualInicioY, visualInicioX)) != Aire):

                visualInicioY = self.inicioPeladoY()
                visualInicioX = self.inicioPeladoX()
        self.visualInicioX = visualInicioX
        self.visualInicioY = visualInicioY

    def getvisualInicioX(self):
        return self.visualInicioX
    
    def getVisualInicioY(self):
        return self.visualInicioY