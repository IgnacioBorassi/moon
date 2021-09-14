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
        self.sizeX = 216
        self.sizeY = 104
        self.celdasX = 216
        self.celdasY = 104
        self.visualInicioY = None
        self.visualInicioX = None
        self.menu = Menu()
        self.mundo = Mundo(self.sizeX, self.sizeY)
        self.escalaX = 40
        self.escalaY = 40




    def inicioCeldaYOP(self, y):
        '''Calculo para centrar la pantalla'''
        return (y * - 40) + 40*6

    def inicioCeldaXOP(self, x):
        '''Calculo para centrar la pantalla'''
        return (x * - 40) + 40*13

    def getInicioCeldaX(self):
        return self.inicioCeldaX
    
    def getInicioCeldaY(self):
        return self.inicioCeldaY
    
    def getVisualInicioY(self):
        return self.visualInicioY
    
    def getVisualInicioX(self):
        return self.visualInicioX

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
                    print ("nashe")
                    self.menu.apagarMenu()
                elif self.menu.getExitRect().collidepoint(event.pos):
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    self.menu.prenderMenu()
                if self.menu.getActivo() == False:
                    if event.key == pygame.K_j:
                        self.inicioCeldaY = (self.visualInicioY * -40) + 40*6
                        self.inicioCeldaX = (self.visualInicioX * -40) + 40*13

                    if event.key == pygame.K_DOWN:
                        self.inicioCeldaY -= self.escalaY
                        if self.inicioCeldaY < -3640:
                            self.inicioCeldaY = -3640
                    
                        print("Eje Y Lista: "+str(self.inicioCeldaY))
                        print("Eje X Lista: "+str(self.inicioCeldaX))
                    
                    if event.key == pygame.K_s:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioY +=1
                        if self.visualInicioY > 101:
                            self.visualInicioY = 101
                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                        and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Aire):
                            print(type(self.mundo.getTerreno(self.visualInicioY,self.visualInicioX)))
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                            self.mundo.cambiarVisual(self.visualInicioY, self.visualInicioX, True)
                            self.mundo.cambiarVisual(self.visualInicioY, (self.visualInicioX + 1), True)
                            self.mundo.cambiarVisual(self.visualInicioY, (self.visualInicioX - 1), True)
                            self.mundo.cambiarVisual(self.visualInicioY + 1, self.visualInicioX, True)
                            self.mundo.cambiarVisual((self.visualInicioY + 1), (self.visualInicioX + 1), True)
                            self.mundo.cambiarVisual((self.visualInicioY + 1), (self.visualInicioX - 1), True)
                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))
                        else:
                            self.visualInicioY -= 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)

                    if event.key == pygame.K_UP:
                        self.inicioCeldaY += self.escalaY
                        if self.inicioCeldaY > 0:
                            self.inicioCeldaY = 0
                        
                        print("Eje Y Lista: "+str(self.inicioCeldaY))
                        print("Eje X Lista: "+str(self.inicioCeldaX))

                    if event.key == pygame.K_w:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioY -=1
                        if self.visualInicioY < 1:
                            self.visualInicioY = 1
                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                        and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Aire):

                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                            print(type(self.mundo.getTerreno(self.visualInicioY,self.visualInicioX)))

                            self.mundo.cambiarVisual(self.visualInicioY, self.visualInicioX, True)
                            self.mundo.cambiarVisual(self.visualInicioY, (self.visualInicioX + 1), True)
                            self.mundo.cambiarVisual(self.visualInicioY, (self.visualInicioX - 1), True)
                            self.mundo.cambiarVisual((self.visualInicioY - 1), self.visualInicioX, True)
                            self.mundo.cambiarVisual((self.visualInicioY - 1), (self.visualInicioX + 1), True)
                            self.mundo.cambiarVisual((self.visualInicioY - 1), (self.visualInicioX - 1), True)
                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))
                        else:
                            self.visualInicioY += 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)

                    if event.key == pygame.K_RIGHT:
                        self.inicioCeldaX -= self.escalaX
                        if self.inicioCeldaX < -7560:
                            self.inicioCeldaX = -7560
                        
                        print("Eje Y Lista: "+str(self.inicioCeldaY))
                        print("Eje X Lista: "+str(self.inicioCeldaX))

                    if event.key == pygame.K_d:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioX +=1
                        if self.visualInicioX > 213:
                            self.visualInicioX = 213
                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra 
                        and type(self.mundo.getNaturaleza(self.visualInicioY, self.visualInicioX)) == Aire):

                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                            print(type(self.mundo.getTerreno(self.visualInicioY,self.visualInicioX)))

                            self.mundo.cambiarVisual(self.visualInicioY, self.visualInicioX, True)
                            self.mundo.cambiarVisual((self.visualInicioY - 1), self.visualInicioX, True)
                            self.mundo.cambiarVisual((self.visualInicioY + 1), self.visualInicioX, True)
                            self.mundo.cambiarVisual(self.visualInicioY, (self.visualInicioX + 1), True)
                            self.mundo.cambiarVisual((self.visualInicioY - 1), self.visualInicioX + 1, True)
                            self.mundo.cambiarVisual((self.visualInicioY + 1), self.visualInicioX + 1, True)
                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))
                        else:
                            self.visualInicioX -= 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)

                    if event.key == pygame.K_LEFT:
                        self.inicioCeldaX += self.escalaX
                        if self.inicioCeldaX > 0:
                            self.inicioCeldaX = 0

                        print("Eje Y Lista: "+str(self.inicioCeldaY))
                        print("Eje X Lista: "+str(self.inicioCeldaX))

                    if event.key == pygame.K_a:
                        self.mundo.sacarPelado(self.visualInicioY, self.visualInicioX)
                        self.visualInicioX -=1
                        if self.visualInicioX < 1:
                            self.visualInicioX = 1
                        if (type(self.mundo.getTerreno(self.visualInicioY, self.visualInicioX)) == Tierra and type(self.mundo.getNaturaleza(self.visualInicioY,self.visualInicioX)) == Aire):
                        
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
                            print(type(self.mundo.getTerreno(self.visualInicioY,self.visualInicioX)))

                            self.mundo.cambiarVisual(self.visualInicioY, self.visualInicioX, True)
                            self.mundo.cambiarVisual((self.visualInicioY - 1), self.visualInicioX, True)
                            self.mundo.cambiarVisual((self.visualInicioY + 1), self.visualInicioX, True)
                            self.mundo.cambiarVisual(self.visualInicioY, (self.visualInicioX - 1), True)
                            self.mundo.cambiarVisual((self.visualInicioY - 1), self.visualInicioX - 1, True)
                            self.mundo.cambiarVisual((self.visualInicioY + 1), self.visualInicioX - 1, True)
                            print("Eje Y Descubridor: " + str(self.visualInicioY))
                            print("Eje X Descubridor: " + str(self.visualInicioX))
                        else: 
                            self.visualInicioX += 1
                            self.mundo.ponerPelado(self.visualInicioY, self.visualInicioX)
        
    
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
    

    def getTerreno(self, y, x):
        return self.mundo.getTerreno(y, x)
    
    def getNaturaleza(self, y, x):
        return self.mundo.getNaturaleza(y,x)
    

    def zonaInicial(self, y, x):
        self.mundo.zonaInicial(y, x)

    def cambiarVisual(self, y, x, nuevoVisual):
        self.mundo.cambiarVisual(y,x,nuevoVisual)

    def ponerPelado(self, y, x):
        self.mundo.ponerPelado(y, x)
    

    def getVisual(self, y, x):
        return self.mundo.getVisual(y,x)
    
    def getTerreno(self, y, x):
        return self.mundo.getTerreno(y,x)

    def getNaturaleza(self, y, x):
        return self.mundo.getNaturaleza(y,x)
    
    def getPelado(self, y, x):
        return self.mundo.getPelado(y,x)
    

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