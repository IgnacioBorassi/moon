from agua import Agua
from aire import Aire
import pygame, sys, random
from casa import Casa
from marcador import Marcador
from mundo import Mundo
from arbol import Arbol
from tierra import Tierra
from montana import Montana
from menu import Menu
from modo import Modo
from persona import Persona
import time
import os

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
        self.modo = Modo()
        self.mundo = Mundo(self.celdasX, self.celdasY)
        self.escalaX = 40
        self.escalaY = 40
        self.seleccion = False
        self.activar = False
        self.ordenSeleccion = -1
        self.cantMarcadores = -1
        self.cantNoMarcados = -1
        self.mapa1 = None
        self.mapa2 = None
        self.mapaG = None

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

    def getCantMarcadores(self):
        self.cantMarcadores = -1
        self.cantNoMarcados = -1
        for i in range(1, (self.celdasY - 1)):
            for x in range(1, (self.celdasX - 1)):
                if self.mundo.getOrdenMarcador(i, x) != -1:
                    self.cantMarcadores += 1
                    self.cantNoMarcados += 1
    
    def realizarAcciones(self):
        if (self.cantMarcadores - self.cantNoMarcados) == (self.cantMarcadores + 1):
            self.activar == False
            self.cantMarcadores = -1000
            self.cantNoMarcados = -1000
            self.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)
            self.ordenSeleccion = -1
            self.seleccion = False
            self.sacarMarcadores()
            if self.mundo.getEnergia() == 0:
                self.mundo.setEnergia()
            

        if self.activar == True:
            for i in range(1, (self.celdasY - 1)):
                for x in range(1, (self.celdasX - 1)):
                    if self.mundo.getOrdenMarcador(i, x) == (self.cantMarcadores - self.cantNoMarcados):
                        
                        if (self.cantMarcadores - self.cantNoMarcados) == 0:
                            self.cantNoMarcados -= 1
                            if self.getPelado(i, x) == True:
                                self.ponerPelado(i, x)
                                return
                            else:
                                print("Error: Se necesita haber seleccionado un pelado")
                                self.cantNoMarcados = -1
                                return
                        else:
                            self.cantNoMarcados -= 1
                            if self.getPelado(i - 1, x) == True and self.getMarcador(i - 1, x) == True:
                                self.sacarPelado(i - 1, x)
                            elif self.getPelado(i + 1, x) == True and self.getMarcador(i + 1, x) == True:
                                self.sacarPelado(i + 1, x)
                            elif self.getPelado(i, x - 1) == True and self.getMarcador(i, x - 1) == True:
                                self.sacarPelado(i, x - 1)
                            elif self.getPelado(i, x + 1) == True and self.getMarcador(i, x + 1) == True:
                                self.sacarPelado(i, x + 1)
                            self.ponerPelado(i, x)
                            self.mundo.cambiarVisualMov(i, x)
                            print(str(repr(self.getNaturaleza(i, x))))
                            if (repr(self.getNaturaleza(i, x))) == "Arbol": 
                                cantMadera = self.mundo.cantidadMaterial(i, x)
                                print(cantMadera)
                                self.mundo.agregarMadera(cantMadera)
                                self.mundo.sacarArbol(i, x)
                                
                                

                            if (repr(self.getNaturaleza(i, x))) == "Montana":
                                piedra = self.mundo.cantidadMaterial(i, x)
                                print(piedra)
                                self.mundo.agregarPiedra(piedra)
                            time.sleep(0.7)
                            return
        




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
                if self.modo.getActivo()== None or self.modo.getActivo()== False:
                    if self.menu.getStartRect().collidepoint(event.pos):
                        if self.modo.getActivo() == None:
                            self.menu.apagarMenu()
                            self.modo.activarModo()
                        else:
                            self.menu.apagarMenu()
                            
                    elif self.menu.getExitRect().collidepoint(event.pos):
                        pygame.quit()
                        exit()
                else:
                    if self.modo.getBotonMapa1Rect().collidepoint(event.pos):
                        self.mapa1 = True
                        
                        self.modo.apagarModo()

                        
                    elif self.modo.getBotonMapa2Rect().collidepoint(event.pos):
                        self.mapa2 = True
                        
                        self.modo.apagarModo()

                    elif self.modo.getBotonMapaGRect().collidepoint(event.pos):
                        self.mapaG = True
                        
                        self.modo.apagarModo()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu.prenderMenu()

                if self.menu.getActivo() == False:
                    if event.key == pygame.K_1:
                        if ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX))) == "Tierra"
                        and (repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX))) == "Aire"):
                            if self.mundo.getMadera() >= 20 and self.mundo.getPiedra() >= 10:
                                self.mundo.ponerCasa(self.visualInicioY, self.visualInicioX)
                                self.mundo.hacerCasa()
                            else:
                                print("te faltan recursos panflin")
                    
                    if event.key == pygame.K_2:
                        self.mundo.hacerBarco()
                            
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
                            self.getCantMarcadores()
                            self.activar = True
                        else:
                            self.activar = False
                            self.ordenSeleccion = 0
                            self.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)
                            self.seleccion = True


                    if event.key == pygame.K_p:
                        with open("guardado.txt", "w") as archivo:
                            for i in range(0, self.celdasY):
                                for x in range(0, self.celdasX):
                                    if self.mundo.getVisual(i, x) == True:
                                        archivo.write('V')
                                    if ((repr(self.getTerreno(i, x)))) == "Tierra":
                                        if ((repr(self.getNaturaleza(i, x)))) == "Arbol":
                                            if x == self.celdasX:
                                                archivo.write('Arbol')
                                            else:
                                                archivo.write('Arbol,')
                                        elif ((repr(self.getNaturaleza(i, x)))) == "Montana":
                                            if x == self.celdasX:
                                                archivo.write('Montana')
                                            else:
                                                archivo.write('Montana,')
                                        elif ((repr(self.getNaturaleza(i, x)))) == "Aire":  
                                                             
                                            if (self.mundo.getCasa(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('Casa')
                                                else:
                                                    archivo.write('Casa,')
                                            elif (self.mundo.getPelado(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('Persona')
                                                else:
                                                    archivo.write('Persona,')
                                            else:
                                                if x == self.celdasX:
                                                    archivo.write('Tierra')
                                                else:
                                                    archivo.write('Tierra,') 
                                    else:
                                        if x == self.celdasX:
                                            archivo.write('Agua')
                                        else:
                                            archivo.write('Agua,')
                                
                                archivo.write("\n")
                    
                    if event.key == pygame.K_w:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                            self.ordenSeleccion = -1
                            self.visualInicioY -= 1
                        else:
                            if self.getMarcador(self.visualInicioY - 1, self.visualInicioX) == True:
                                
                                print("No podes pasar por arriba de otro marcador")
                            else:
                                if self.mundo.getEnergia() == 0:
                                    print("ya esta men")
                                else:
                                    if ((repr(self.getTerreno(self.visualInicioY - 1, self.visualInicioX)))) == "Tierra":
                                        if ((repr(self.getNaturaleza(self.visualInicioY - 1, self.visualInicioX)))) == "Arbol":
                                            self.mundo.restarEnergia(100)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY -= 1

                                        elif ((repr(self.getNaturaleza(self.visualInicioY - 1 , self.visualInicioX)))) == "Aire":
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY -= 1 

                                        elif ((repr(self.getNaturaleza(self.visualInicioY - 1 , self.visualInicioX)))) == "Montana":
                                            self.mundo.restarEnergia(150)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY -= 1
                                    
                                    elif ((repr(self.getTerreno(self.visualInicioY - 1, self.visualInicioX)))) == "Agua":  
                                        if self.mundo.getBarco()== True:
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY -= 1
                                        else:
                                            print("No tienes barco")
                            

                        if self.visualInicioY < 1:
                            self.visualInicioY = 1
                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion) 

                    if event.key == pygame.K_a:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                            self.ordenSeleccion = -1
                            self.visualInicioX -= 1
                        else:
                            if self.getMarcador(self.visualInicioY, self.visualInicioX - 1) == True:
                                print("No podes ir a la izquierda si ya hay un marcador")
                            else:
                                if self.mundo.getEnergia() == 0:
                                    print("ya esta men, estoy muy cansado")
                                else:
                                    if ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX - 1)))) == "Tierra":
                                        if ((repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX - 1)))) == "Arbol":
                                            self.mundo.restarEnergia(100)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX -= 1
                                        elif ((repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX - 1 )))) == "Aire":
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX -= 1
                                        elif ((repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX - 1 ))))== "Montana":
                                            self.mundo.restarEnergia(150)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX -= 1
                                    elif ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX - 1)))) == "Agua":  
                                        if self.mundo.getBarco()== True:
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX -= 1
                                        else:
                                            print("No tienes barco")
                            
                        if self.visualInicioX < 1:
                            self.visualInicioX = 1
                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)

                    if event.key == pygame.K_s:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                            self.ordenSeleccion = -1
                            self.visualInicioY += 1
                        else:
                            if self.getMarcador(self.visualInicioY + 1, self.visualInicioX) == True:
                                print("No podes ir para abajo si ya hay un marcador")
                            else:
                                if self.mundo.getEnergia() == 0:
                                    print("ya esta men")
                                else:
                                    if ((repr(self.getTerreno(self.visualInicioY + 1, self.visualInicioX)))) == "Tierra":
                                        if ((repr(self.getNaturaleza(self.visualInicioY + 1 , self.visualInicioX)))) == "Arbol":
                                            self.mundo.restarEnergia(100)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY += 1
                                        elif ((repr(self.getNaturaleza(self.visualInicioY + 1, self.visualInicioX)))) == "Aire":
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY += 1
                                        elif ((repr(self.getNaturaleza(self.visualInicioY + 1, self.visualInicioX)))) == "Montana":
                                            self.mundo.restarEnergia(150)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY += 1
                                    elif ((repr(self.getTerreno(self.visualInicioY + 1, self.visualInicioX)))) == "Agua":  
                                        if self.mundo.getBarco()== True:
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioY += 1
                                        else:
                                            print("no tienes barco")
                                    

                        if self.visualInicioY > (self.celdasY - 3):
                            self.visualInicioY = (self.celdasY - 3)

                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)

                    if event.key == pygame.K_d:
                        if self.seleccion == False:
                            self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                            self.ordenSeleccion = -1
                            self.visualInicioX += 1
                        else:
                            if self.getMarcador(self.visualInicioY, self.visualInicioX + 1) == True:
                                print("No da ir a la derecha si ya hay un marcador")
                            else:
                                if self.mundo.getEnergia() == 0:
                                    print("ya esta men")
                                else:
                                    if ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX + 1)))) == "Tierra":
                                        if ((repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX + 1)))) == "Arbol":
                                            self.mundo.restarEnergia(100)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX += 1
                                        elif ((repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX + 1)))) == "Aire":
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX += 1
                                        elif ((repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX + 1)))) == "Montana":
                                            self.mundo.restarEnergia(150)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX += 1
                                    elif ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX + 1)))) == "Agua":  
                                        if self.mundo.getBarco()== True:
                                            self.mundo.restarEnergia(50)
                                            self.ordenSeleccion += 1
                                            self.visualInicioX += 1
                                        else:
                                            print("no tienes barco")
                                    

                        if self.visualInicioX > (self.celdasX - 3):
                            self.visualInicioX = (self.celdasX - 3)
                        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)

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

    def colocarCivilizacion(self, y, x):
        self.mundo.colocarCivilizacion(y, x)

    def cambiarVisual(self, y, x, nuevoVisual):
        self.mundo.cambiarVisual(y, x, nuevoVisual)

    def ponerPelado(self, y, x):
        self.mundo.ponerPelado(y, x)
    
    def sacarPelado(self, y, x):
        self.mundo.sacarPelado(y, x)

    def ponerMarcador(self, y, x, nuevoOrden):
        self.mundo.ponerMarcador(y, x, nuevoOrden)

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
        while ((repr(self.getTerreno(visualInicioY, visualInicioX))) != "Tierra" or 
        (repr(self.getNaturaleza(visualInicioY, visualInicioX))) != "Aire"):
            visualInicioY = self.inicioPeladoY()
            visualInicioX = self.inicioPeladoX()

        self.visualInicioX = visualInicioX
        self.visualInicioY = visualInicioY

    def sacarMarcadores(self):
        for i in range(0, self.celdasY):
            for x in range(0, self.celdasX):
                self.mundo.sacarMarcador(i, x)
        self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)


    def getvisualInicioX(self):
        return self.visualInicioX
    
    def getVisualInicioY(self):
        return self.visualInicioY

    def getMundoVisualX(self):
        return self.mundo.getInicioX()

    def getMundoVisualY(self):
        return self.mundo.getInicioY()

    def cargarMapa(self):
        self.mundo.cargarMapa()
    
    def cargarMapaG(self):
        self.mundo.cargarMapaG()

    def getModoActivo(self):
        return self.modo.getActivo()
    
    def getFondoModo(self):
        return self.modo.getFondoModo()
    
    def getBotonMapa1Sup(self):
        return self.modo.getBotonMapa1Sup()
    
    def getBotonMapa1Rect(self):
        return self.modo.getBotonMapa1Rect()
    
    def getBotonMapa2Sup(self):
        return self.modo.getBotonMapa2Sup()
    
    def getBotonMapa2Rect(self):
        return self.modo.getBotonMapa2Rect()
    
    def getBotonMapaGSup(self):
        return self.modo.getBotonMapaGSup()
    
    def getBotonMapaGRect(self):
        return self.modo.getBotonMapaGRect()
    
    def cargarMapa1(self):
        self.mundo.cargarMapa1()
    
    def cargarMapa2(self):
        self.mundo.cargarMapa2()
    
    def getMapaG(self):
        return self.mapaG
    
    def getMapa1(self):
        return self.mapa1
    
    def getMapa2(self):
        return self.mapa2
    
    def sacarValoresMapas(self):
        self.mapa1 = False
        self.mapa2 = False
        self.mapaG = False
    
    def getMadera(self):
        return str(self.mundo.getMadera())
    
    def getEnergia(self):
        return str(self.mundo.getEnergia())

    def getPiedra(self):
        return str(self.mundo.getPiedra())
    
    def getBarco(self):
        return self.mundo.getBarco()
    
    def restarUsoBarco(self):
        self.mundo.restarUsoBarco()
    
    def getUsoBarco(self):
        return str(self.mundo.getUsosBarco())