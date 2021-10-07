from celda import  Celda 
import pygame
import random
from arbol import Arbol
from tierra import Tierra
from aire import Aire
from agua import Agua
from montana import Montana
import time

class Mundo():
    '''El mundo con sus rios, arboles, montanas y pelado'''

    def __init__(self, cantCeldasX, cantCeldasY):
        self.coordenadas = []
        self.cantCeldasX = cantCeldasX
        self.cantCeldasY = cantCeldasY
        self.inicioCeldaX = None
        self.inicioCeldaY = None
        self.crearMundo()


    def generarTerreno(self):
        '''Completa toda la matriz con agua o tierra'''

        milistaCopada = []

        for i in range(0, self.cantCeldasY):
            milistaCopada.append([])
            for x in range(0, self.cantCeldasX):
                randomN = int(random.randrange(0, 40))

                if randomN in [0, 1, 2, 3, 4, 5, 6]:
                    milistaCopada[i].append(Celda(Agua(Aire(), None), None, False, randomN))
                else:
                    milistaCopada[i].append(Celda(Tierra(Aire(), None), None, False, randomN))
        return milistaCopada
    
    def cargarMapa(self): 

        archivo = open("guardado.txt")
        self.coordenadas = []

        for position, line in enumerate(archivo):
            line = line.split(',')
            line.pop()
            self.coordenadas.append(line)

        for i in range(0, (self.cantCeldasY)):
            for x in range(0, (self.cantCeldasX)):
                if self.coordenadas[i][x] == "Tierra":
                    self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), None, False, 0))
                if self.coordenadas[i][x] == "Agua":
                    self.coordenadas[i][x] = (Celda(Agua(Aire(), None), None, False, 0))
                if self.coordenadas[i][x] == "Arbol":
                    self.coordenadas[i][x] = (Celda(Tierra(Arbol(), None), None, False, 0))
                if self.coordenadas[i][x] == "Montana":
                    self.coordenadas[i][x] = (Celda(Tierra(Montana(), None), None, False, 0))
                if self.coordenadas[i][x] == "Casa":
                    self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), None, False, 0))
                    self.coordenadas[i][x].ponerCasa()
                if self.coordenadas[i][x] == "Persona":
                    self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), None, False, 0))
                    self.coordenadas[i][x].ponerPelado()
                if self.coordenadas[i][x] == "VTierra":
                    self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), None, True, 0))
                if self.coordenadas[i][x] == "VAgua":
                    self.coordenadas[i][x] = (Celda(Agua(Aire(), None), None, True, 0))
                if self.coordenadas[i][x] == "VArbol":
                    self.coordenadas[i][x] = (Celda(Tierra(Arbol(), None), None, True, 0))
                if self.coordenadas[i][x] == "VMontana":
                    self.coordenadas[i][x] = (Celda(Tierra(Montana(), None), None, True, 0))
                if self.coordenadas[i][x] == "VCasa":
                    self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), None, True, 0))
                    self.coordenadas[i][x].ponerCasa()
                if self.coordenadas[i][x] == "VPersona":
                    self.inicioCeldaX = x
                    self.inicioCeldaY = i
                    self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), None, True, 0))
                    self.coordenadas[i][x].ponerPelado()
        print(self.inicioCeldaX)
    def modificarMundo(self, listacopada):
        '''Modifica pedazos de agua y tierra'''

        otraLista = listacopada

        for i in range(1, (self.cantCeldasY - 1)):
            for x in range(1, (self.cantCeldasX - 1)):
                if type(listacopada[i][x].getTerreno()) == Tierra:
                    if (type(listacopada[i - 1][x].getTerreno()) == Agua and 
                    type(listacopada[i + 1][x].getTerreno()) == Agua):

                        otraLista[i][x].cambiarTerreno(Agua(Aire(), None))
                        
                    elif (type(listacopada[i][x - 1].getTerreno()) == Agua and 
                    type(listacopada[i][x + 1].getTerreno()) == Agua):
                        otraLista[i][x].cambiarTerreno(Agua(Aire(), None))

        self.coordenadas = otraLista

        for i in range(1,(self.cantCeldasY - 1)):
            for x in range(1,(self.cantCeldasX - 1)):
                if type(otraLista[i][x].getTerreno()) == Agua:
                    if (type(otraLista[i - 1][x].getTerreno()) == Tierra and type(otraLista[i + 1][x].getTerreno()) == Tierra and  type(otraLista[i][x - 1].getTerreno()) == Tierra and type(otraLista[i][x + 1].getTerreno()) == Tierra):

                        self.coordenadas[i][x].cambiarTerreno(Tierra(Aire(), None))


    def agregarNaturaleza(self):
        '''Genera en las coordenadas, donde haya tierra, una montana o un arbol'''

        for i in range(0, self.cantCeldasY):
            for x in range(0, self.cantCeldasX):
                if (type(self.coordenadas[i][x].getTerreno()) == Tierra and 
                self.coordenadas[i][x].getNum() in [9, 10]):
                    self.coordenadas[i][x].cambiarNaturaleza(Montana())

                elif (type(self.coordenadas[i][x].getTerreno()) == Tierra and 
                self.coordenadas[i][x].getNum() in [11, 12, 13, 14, 15, 16, 17]):
                    self.coordenadas[i][x].cambiarNaturaleza(Arbol())


    def realizarAcciones(self):
        cantMarcadores = -1
        for i in range(1, (self.cantCeldasY - 1)):
            for x in range(1, (self.cantCeldasX - 1)):
                if self.getOrdenMarcador(i, x) != -1:
                    cantMarcadores += 1
        for cant in range(0, cantMarcadores + 1):
            for i in range(1, (self.cantCeldasY - 1)):
                for x in range(1, (self.cantCeldasX - 1)):
                    if self.getOrdenMarcador(i, x) == cant:
                        self.ponerPelado(i,x)
                        time.sleep(2)
                        self.sacarPelado(i,x)



    def crearMundo(self):
        '''Crea el mundo'''

        self.modificarMundo(self.generarTerreno())
        self.agregarNaturaleza()


    def getTerreno(self, y, x):
        return self.coordenadas[y][x].getTerreno()

    def getNaturaleza(self, y, x):
        return self.coordenadas[y][x].getNaturaleza()

    def getVisual(self, y, x):
        return self.coordenadas[y][x].getVisual()
    
    def cambiarVisual(self, y, x, nuevoVisual):
        return self.coordenadas[y][x].cambiarVisual(nuevoVisual)
    
    def ponerPelado(self, y, x):
        return self.coordenadas[y][x].ponerPelado()
    
    def ponerMarcador(self, y, x, nuevoOrden):
        return self.coordenadas[y][x].ponerMarcador(nuevoOrden)

    def sacarPelado(self, y, x):
        return self.coordenadas[y][x].sacarPelado()

    def sacarMarcador(self, y, x):
        return self.coordenadas[y][x].sacarMarcador()

    def getPelado(self, y, x):
        return self.coordenadas[y][x].getPelado()

    def getMarcador(self, y, x):
        return self.coordenadas[y][x].getMarcador()

    def getCasa(self, y, x):
        return self.coordenadas[y][x].getCasa()

    def ponerCasa(self, y, x):
        return self.coordenadas[y][x].ponerCasa()

    def getOrdenMarcador(self, y, x):
        return self.coordenadas[y][x].getOrdenMarcador()

    def getInicioX(self):
        return self.inicioCeldaX
    
    def getInicioY(self):
        return self.inicioCeldaY

    def zonaInicial(self, y, x):
        '''Muestra la zona donde empieza el personaje'''

        for i in range(1, 6):
            self.cambiarVisual(y + i, x, True)
            self.cambiarVisual(y - i, x, True)
            self.cambiarVisual(y, x + i, True)
            self.cambiarVisual(y, x - i, True)
            for e in range(1, 6):
                self.cambiarVisual(y + i, x + e, True)
                self.cambiarVisual(y + i, x - e, True)
                self.cambiarVisual(y - i, x + e, True)
                self.cambiarVisual(y - i, x - e, True)
 

    def cambiarVisualX(self, visualInicioY, visualInicioX, direccion):
        '''Hace visibles el alrededor del personaje segun la direccion en x'''

        self.ponerPelado(visualInicioY, visualInicioX)
        self.cambiarVisual(visualInicioY, visualInicioX, True)
        self.cambiarVisual((visualInicioY - 1), visualInicioX, True)
        self.cambiarVisual((visualInicioY + 1), visualInicioX, True)
        self.cambiarVisual(visualInicioY, (visualInicioX + direccion), True)
        self.cambiarVisual((visualInicioY - 1), visualInicioX + direccion, True)
        self.cambiarVisual((visualInicioY + 1), visualInicioX + direccion, True)


    def cambiarVisualY(self, visualInicioY, visualInicioX, direccion):
        '''Hace visibles el alrededor del personaje segun la direccion en y'''
        
        self.ponerPelado(visualInicioY, visualInicioX)
        self.cambiarVisual(visualInicioY, visualInicioX, True)
        self.cambiarVisual(visualInicioY, (visualInicioX + 1), True)
        self.cambiarVisual(visualInicioY, (visualInicioX - 1), True)
        self.cambiarVisual((visualInicioY + direccion), visualInicioX, True)
        self.cambiarVisual((visualInicioY + direccion), (visualInicioX + 1), True)
        self.cambiarVisual((visualInicioY + direccion), (visualInicioX - 1), True)

    def sacarArbol(self, y, x):
        self.coordenadas[y][x].sacarArbol()
    
    def cantidadMaterial(self, y, x):
        return self.coordenadas[y][x].randomMaterial()

    # def traducirMapa(self): 

    #     for i in range(0, self.celdasY):
    #         for x in range(0, self.celdasX):
    #             for f in self.coordenadas: