from agua import Agua
from aire import Aire
import pygame, sys, random
from arquero import Arquero
from casa import Casa
from fundador import Fundador
from guerrero import Guerrero
from obrero import Obrero
from marcador import Marcador
from mundo import Mundo
from arbol import Arbol
from tierra import Tierra
from montana import Montana
from menu import Menu
from modo import Modo
from persona import Persona
from pantallaFinal import PantallaFinal
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
        self.pantallaFinal = PantallaFinal()
        self.mundo = Mundo(self.celdasX, self.celdasY)
        self.escalaX = 40
        self.escalaY = 40
        self.seleccion = False
        self.activar = False
        self.ordenSeleccion = -1
        self.cantMarcadores = -1
        self.cantNoMarcados = -1
        self.visualMov = True
        self.clase = None
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

    def getPuerto(self, y, x):
        return self.mundo.getPuerto(y, x)

    def getCorral(self, y, x):
        return self.mundo.getCorral(y, x)

    def getCultivo(self, y, x):
        return self.mundo.getCultivo(y, x)
        
    def getMina(self, y, x):
        return self.mundo.getMina(y, x)

    def getCantMarcadores(self):
        self.cantMarcadores = -1
        self.cantNoMarcados = -1
        for i in range(1, (self.celdasY - 1)):
            for x in range(1, (self.celdasX - 1)):
                if self.mundo.getOrdenMarcador(i, x) != -1:
                    self.cantMarcadores += 1
                    self.cantNoMarcados += 1
    
    def bordeVisual(self, y, x):
       return self.mundo.tipoBorde(y, x)
                

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
                self.mundo.setTurno()
                if (self.mundo.getCantTurno() % 2) == 0:
                    self.mundo.turnoPeludo()
                self.mundo.setEnergia(500)
                self.mundo.setTurno()
                self.mundo.restarComida(self.mundo.contarPelados()*3)
            if self.mundo.getComida() == 0:
                self.mundo.setComida(30)

        if self.activar == True:
            for i in range(1, (self.celdasY - 1)):
                for x in range(1, (self.celdasX - 1)):
                    

                    if self.mundo.getOrdenMarcador(i, x) == (self.cantMarcadores - self.cantNoMarcados):
                        
                        
                        if (self.cantMarcadores - self.cantNoMarcados) == 0:
                            self.clase = self.chequearClase(i, x)
                            
                            self.cantNoMarcados -= 1
                            if self.getPelado(i, x) == True:
                                
                                self.ponerPelado(i, x, self.clase)
                                
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
                            
                            self.ponerPelado(i, x, self.clase)
                            
                            self.mundo.cambiarVisualMov(i, x, self.visualMov)
                            if (repr(self.getClase(i, x))) == "Obrero":

                                if (repr(self.getNaturaleza(i, x))) == "Arbol": 
                                    cantMadera = self.mundo.cantidadMaterial(i, x)
                                    self.mundo.agregarMadera(cantMadera)
                                    self.mundo.sacarArbol(i, x)
                                    
                                    
                                if self.getMina(i, x) == True:
                                    piedra = self.mundo.cantidadMaterial(i, x)
                                    self.mundo.agregarPiedra(piedra)
                                    print(piedra)
                                
                                if self.getPuerto(i, x) == True:
                                    comida = self.mundo.cantidadMaterial(i, x)
                                    self.mundo.agregarComida(comida)
                                    print(comida)
                                
                                if self.getCorral(i, x) == True:
                                    comida = self.mundo.cantidadMaterialCorral(i, x)
                                    self.mundo.agregarComida(comida)
                                    print(comida)
                                
                                if self.getCultivo(i, x) == True:
                                    comida = self.mundo.cantidadMaterialCultivo(i, x)
                                    self.mundo.agregarComida(comida)
                                    print(comida)
                            
                            if (repr(self.getTerreno(i, x))) == "Agua":
                                self.mundo.restarUsoBarco()

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
                if self.pantallaFinal.getActivo() == True:
                    if self.pantallaFinal.getReiniciarRect().collidepoint(event.pos):
                        self.mundo.destruirMundo()
                        self.mundo.reiniciarTurnos()
                        self.modo.activarModo()
                        self.pantallaFinal.apagarFinal()
                            
                    elif self.pantallaFinal.getCerrarRect().collidepoint(event.pos):
                        pygame.quit()
                        exit()  
                elif self.modo.getActivo() == None and self.menu.getActivo() == True:
                    if self.menu.getStartRect().collidepoint(event.pos):
                        if self.modo.getActivo() == None:
                            self.menu.apagarMenu()
                            self.modo.activarModo()
                        else:
                            self.menu.apagarMenu()
                            
                    elif self.menu.getExitRect().collidepoint(event.pos):
                        pygame.quit()
                        exit()                    
                elif self.modo.getActivo() == True:
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
                        if (repr(self.mundo.getClasePersona(self.visualInicioY, self.visualInicioX))) == "Fundador":
                            self.sacarPelado(self.visualInicioY, self.visualInicioX)
                            if ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX))) == "Tierra"
                            and (repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX))) == "Aire"):
                                
                                self.colocarCivilizacion(visualInicioY, visualInicioX)
                                
                        else:
                            if self.mundo.getConstruccion(self.visualInicioY, self.visualInicioX) != True: 
                                if ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX))) == "Tierra"
                                and (repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX))) == "Aire"):
                                    if self.mundo.getCivilizacion(self.visualInicioY, self.visualInicioX) == 1:
                                        if self.mundo.getMadera() >= 20 and self.mundo.getPiedra() >= 10:
                                            self.mundo.ponerCasa(self.visualInicioY, self.visualInicioX)
                                            self.mundo.hacerCasa()
                                            self.mundo.restarEnergia(20)
                                        
                                        
                                        else:
                                            print("te faltan recursos panflin")
                                    else:
                                        print("No podes construir fuera de tu territorio")

                                elif ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX))) == "Agua"
                                    and (repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX))) == "Aire"):
                                        if self.mundo.getCivilizacion(self.visualInicioY, self.visualInicioX) == 1:
                                            if self.mundo.getMadera() >= 100:
                                                self.mundo.ponerPuerto(self.visualInicioY, self.visualInicioX)
                                                self.mundo.hacerPuerto()
                                                self.mundo.restarEnergia(25)
                                            else:
                                                print("te faltan recursos panflin")

                                elif ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX))) == "Tierra"
                                    and (repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX))) == "Montana"):
                                        if self.mundo.getCivilizacion(self.visualInicioY, self.visualInicioX) == 1:
                                            if self.mundo.getMadera() >= 40:
                                                self.mundo.ponerMina(self.visualInicioY, self.visualInicioX)
                                                self.mundo.hacerMina()
                                                self.mundo.restarEnergia(30)
                                            else:
                                                print("te faltan recursos panflin")
                                        else:
                                            print("No podes construir fuera de tu territorio")
                    
                    if event.key == pygame.K_2:
                        self.mundo.hacerBarco()
                    
                    if event.key == pygame.K_3:
                        if self.mundo.getConstruccion(self.visualInicioY, self.visualInicioX) != True: 
                            if ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX))) == "Tierra"
                                and (repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX))) == "Aire"):
                                    if self.mundo.getCivilizacion(self.visualInicioY, self.visualInicioX) == 1:
                                        if self.mundo.getMadera() >= 20:
                                            self.mundo.ponerCorral(self.visualInicioY, self.visualInicioX)
                                            self.mundo.hacerCorral()
                                        else: 
                                            print("te faltan recursos panflin")
                                    else:
                                        print("No podes construir fuera de tu territorio")
                        
                    if event.key == pygame.K_4:
                        if self.mundo.getConstruccion(self.visualInicioY, self.visualInicioX) != True: 
                            if ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX))) == "Tierra"
                                and (repr(self.getNaturaleza(self.visualInicioY, self.visualInicioX))) == "Aire"):
                                    if self.mundo.getCivilizacion(self.visualInicioY, self.visualInicioX) == 1:
                                        if self.mundo.getMadera() >= 5 and self.mundo.getPiedra() >= 3:
                                            self.mundo.ponerCultivo(self.visualInicioY, self.visualInicioX)
                                            self.mundo.hacerCultivo()
                                        else: 
                                            print("te faltan recursos panflin")
                                    else:
                                        print("No podes construir fuera de tu territorio")
                    
                    if event.key == pygame.K_j:
                        self.inicioCeldaY = ((self.visualInicioY * - self.escalaY) +
                            self.escalaY * int((self.pantallaY/self.escalaY)/2))

                        self.inicioCeldaX = ((self.visualInicioX * - self.escalaX) +
                            self.escalaX * int((self.pantallaX/self.escalaX)/2))

                    if event.key == pygame.K_v:
                        if self.visualMov == True:
                            self.visualMov = False
                        else:
                            self.visualMov = True
                            
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
                        energia = self.getEnergia()
                        comida = self.getComida()
                        barcos = self.getUsoBarco()
                        piedra = self.getPiedra()
                        madera = self.getMadera()
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

                                            if (self.mundo.getMina(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('Mina')
                                                else:
                                                    archivo.write('Mina,')  

                                            if (self.mundo.getCorral(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('Corral')
                                                else:
                                                    archivo.write('Corral,') 
                                            
                                            if (self.mundo.getPuerto(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('Puerto')
                                                else:
                                                    archivo.write('Puerto,')            
                                            
                                            if (self.mundo.getCultivo(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('Cultivo')
                                                else:
                                                    archivo.write('Cultivo,') 
                                            
                                            if (self.mundo.getPeludoCasa(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('CasaPeludo')
                                                else:
                                                    archivo.write('CasaPeludo,')   

                                            elif (self.mundo.getPelado(i, x)) == True:
                                                if (repr(self.getClase(i, x))) == "Guerrero":
                                                    if x == self.celdasX:
                                                        archivo.write('GPersona')
                                                    else:
                                                        archivo.write('GPersona,')
                                                    
                                                elif (repr(self.getClase(i, x))) == "Arquero":
                                                    if x == self.celdasX:
                                                        archivo.write('APersona')
                                                    else:
                                                        archivo.write('APersona,')
                                                   
                                                elif (repr(self.getClase(i, x))) == "Obrero":
                                                    if x == self.celdasX:
                                                        archivo.write('OPersona')
                                                    else:
                                                        archivo.write('OPersona,')

                                                else:
                                                    if x == self.celdasX:
                                                        archivo.write('FPersona')
                                                    else:
                                                        archivo.write('FPersona,')

                                                if (repr(self.mundo.getClasePersona(i, x))) == "Peludo":
                                                    if x == self.celdasX:
                                                        archivo.write('Peludo')
                                                    else:
                                                        archivo.write('Peludo,') 
                                                 
                                            else:
                                                if x == self.celdasX:
                                                    archivo.write('Tierra')
                                                else:
                                                    archivo.write('Tierra,') 
                                    else:
                                        if (self.mundo.getPelado(i, x)) == True:
                                            if (repr(self.getClase(i, x))) == "Guerrero":
                                                if x == self.celdasX:
                                                    archivo.write('AGPersona')
                                                else:
                                                    archivo.write('AGPersona,')
                                                
                                            elif (repr(self.getClase(i, x))) == "Arquero":
                                                if x == self.celdasX:
                                                    archivo.write('AAPersona')
                                                else:
                                                    archivo.write('AAPersona,')
                                                
                                            elif (repr(self.getClase(i, x))) == "Obrero":
                                                if x == self.celdasX:
                                                    archivo.write('AOPersona')
                                                else:
                                                    archivo.write('AOPersona,')
                                            else:
                                                if x == self.celdasX:
                                                    archivo.write('AFPersona')
                                                else:
                                                    archivo.write('AFPersona,')
                                            if (repr(self.mundo.getClasePersona(i, x))) == "Peludo":
                                                if x == self.celdasX:
                                                    archivo.write('APeludo')
                                                else:
                                                    archivo.write('APeludo,')
                                            if (self.mundo.getPuerto(i, x)) == True:
                                                if x == self.celdasX:
                                                    archivo.write('Puerto')
                                                else:
                                                    archivo.write('Puerto,')      
                                        
                                        else:      
                                            if x == self.celdasX:
                                                archivo.write('Agua')
                                            else:
                                                archivo.write('Agua,')
                                
                                archivo.write("\n")
                    
                        with open("materiales.txt", "w") as materiales:
                            materiales.write(energia + ',')
                            materiales.write(comida + ',')
                            materiales.write(madera + ',')
                            materiales.write(piedra + ',')
                            materiales.write(barcos)

                    if event.key == pygame.K_w:
                        if self.mundo.getTurno() == True:
                            if self.seleccion == False:
                                self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                                self.ordenSeleccion = -1
                                self.visualInicioY -= 1
                            else:
                                if self.getMarcador(self.visualInicioY - 1, self.visualInicioX) == True:
                                    
                                    print("No podes pasar por arriba de otro marcador")
                                else:
                                    if self.mundo.getEnergia() == 0:
                                        print("Estoy muy cansado")
                                    elif self.getPelado(self.visualInicioY - 1, self.visualInicioX) == True:
                                        print("Aca ya hay alguien")
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
                                            if self.mundo.getUsosBarco() > 0:
                                                self.mundo.restarEnergia(50)
                                                self.ordenSeleccion += 1
                                                self.visualInicioY -= 1
                                            else:
                                                print("No tienes barco")
                                

                            if self.visualInicioY < 1:
                                self.visualInicioY = 1
                            self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion) 

                    if event.key == pygame.K_a:
                        if self.mundo.getTurno() == True:
                            if self.seleccion == False:
                                self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                                self.ordenSeleccion = -1
                                self.visualInicioX -= 1
                            else:
                                if self.getMarcador(self.visualInicioY, self.visualInicioX - 1) == True:
                                    print("No podes ir a la izquierda si ya hay un marcador")
                                else:
                                    if self.mundo.getEnergia() == 0:
                                        print("Estoy muy cansado")
                                    elif self.getPelado(self.visualInicioY, self.visualInicioX - 1) == True:
                                        print("Aca ya hay alguien")
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
                                                self.mundo.restarComida(5)
                                                self.ordenSeleccion += 1
                                                self.visualInicioX -= 1
                                        elif ((repr(self.getTerreno(self.visualInicioY, self.visualInicioX - 1)))) == "Agua":  
                                            if self.mundo.getUsosBarco() > 0:
                                                self.mundo.restarEnergia(50)
                                                self.ordenSeleccion += 1
                                                self.visualInicioX -= 1
                                            else:
                                                print("No tienes barco")
                                
                            if self.visualInicioX < 1:
                                self.visualInicioX = 1
                            self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)

                    if event.key == pygame.K_s:
                        if self.mundo.getTurno() == True:
                            if self.seleccion == False:
                                self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                                self.ordenSeleccion = -1
                                self.visualInicioY += 1
                            else:
                                if self.getMarcador(self.visualInicioY + 1, self.visualInicioX) == True:
                                    print("No podes ir para abajo si ya hay un marcador")
                                else:
                                    if self.mundo.getEnergia() == 0:
                                        print("Estoy muy cansado")
                                    elif self.getPelado(self.visualInicioY + 1, self.visualInicioX) == True:
                                        print("Aca ya hay alguien")
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
                                            if self.mundo.getUsosBarco() > 0:
                                                self.mundo.restarEnergia(50)
                                                self.ordenSeleccion += 1
                                                self.visualInicioY += 1
                                            else:
                                                print("No tienes barco")
                                        

                            if self.visualInicioY > (self.celdasY - 3):
                                self.visualInicioY = (self.celdasY - 3)

                            self.mundo.ponerMarcador(self.visualInicioY, self.visualInicioX, self.ordenSeleccion)

                    if event.key == pygame.K_d:
                        if self.mundo.getTurno() == True:
                            if self.seleccion == False:
                                self.mundo.sacarMarcador(self.visualInicioY, self.visualInicioX)
                                self.ordenSeleccion = -1
                                self.visualInicioX += 1
                            else:
                                if self.getMarcador(self.visualInicioY, self.visualInicioX + 1) == True:
                                    print("No da ir a la derecha si ya hay un marcador")
                                else:
                                    if self.mundo.getEnergia() == 0:
                                        print("Estoy muy cansado")
                                    elif self.getPelado(self.visualInicioY, self.visualInicioX + 1) == True:
                                        print("Aca ya hay alguien")
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
                                            if self.mundo.getUsosBarco() > 0:
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

    def zonaInicialPeludo(self):
        self.mundo.zonaInicialPeludo()

    def zonaInicial(self, y, x):
        self.mundo.zonaInicial(y, x)

    def colocarCivilizacion(self, y, x):
        self.mundo.colocarCivilizacion(y, x)

    def cambiarVisual(self, y, x, nuevoVisual):
        self.mundo.cambiarVisual(y, x, nuevoVisual)

    def ponerPelado(self, y, x, clase):
        self.mundo.ponerPelado(y, x, clase)
    
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
    
    def getPeludoCasa(self, y, x):
        return self.mundo.getPeludoCasa(y, x)

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
    
    def getComida(self):
        return str(self.mundo.getComida())

    def getBarco(self):
        return self.mundo.getBarco()
    
    def restarUsoBarco(self):
        self.mundo.restarUsoBarco()
    
    def getUsoBarco(self):
        return str(self.mundo.getUsosBarco())
    
    def getFundadorActivo(self):
        return self.mundo.getFundadorActivo()
    
    def getGuerreroActivo(self):
        return self.mundo.getGuerrerorActivo()
    
    def getArqueroActivo(self):
        return self.mundo.getArqueroActivo()
    
    def getObreroActivo(self):
        return self.mundo.getObreroActivo()
    
    def getClase(self, y, x):
        return self.mundo.getClasePersona(y, x)
    
    def chequearClase(self, y, x):
        if (repr(self.getClase(y, x))) == "Guerrero":                          
            clase = Guerrero()
            return clase

        elif (repr(self.getClase(y, x))) == "Arquero":
            clase = Arquero()
            return clase
        
        elif (repr(self.getClase(y, x))) == "Obrero":
            clase = Obrero()
            return clase
        else:
            clase = Fundador()
            return clase
        
    def getCantTurno(self):
        return self.mundo.getCantTurno()
    
    def activarFinal(self):
        self.pantallaFinal.prender()
    
    def getActivoFinal(self):
        return self.pantallaFinal.getActivo()

    def getFondoFinal(self):
        return self.pantallaFinal.getFondo()
    
    def getReiniciarsup(self):
        return self.pantallaFinal.getReiniciarsup()
    
    def getCerrarSup(self):
        return self.pantallaFinal.getCerrarSup()
    
    def getReiniciarRect(self):
        return self.pantallaFinal.getReiniciarRect()
    
    def getCerrarRect(self):
        return self.pantallaFinal.getCerrarRect()
    
    def ganador(self):
        return self.mundo.ganador()