from celda import  Celda 
import pygame
import random
from arbol import Arbol
from tierra import Tierra
from aire import Aire
from agua import Agua
from montana import Montana

class Mundo():
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
                randomN = int(random.randrange(0,40))
                if randomN in [0,1,2,3,4,5,6]:
                    milistaCopada[i].append(Celda(Agua(Aire(), None), "Nadie", False, randomN))
                else:
                    milistaCopada[i].append(Celda(Tierra(Aire(), None), "Nadie", False, randomN))
        
        return milistaCopada

    def modificarMundo(self, listacopada):
        '''Modifica pedazos de agua y tierra'''
        otraLista = listacopada

        for i in range(1, (self.cantCeldasY - 1)):
            for x in range(1, (self.cantCeldasX - 1)):
                if type(listacopada[i][x].getTerreno()) == Tierra:
                    if (type(listacopada[i-1][x].getTerreno()) == Agua and 
                    type(listacopada[i+1][x].getTerreno()) == Agua):

                        otraLista[i][x].cambiarTerreno(Agua(Aire(), None))
                        
                    elif (type(listacopada[i][x-1].getTerreno()) == Agua and 
                    type(listacopada[i][x+1].getTerreno()) == Agua):
                        otraLista[i][x].cambiarTerreno(Agua(Aire(), None))

        self.coordenadas = otraLista

        for i in range(1,(self.cantCeldasY - 1)):
            for x in range(1,(self.cantCeldasX - 1)):
                if type(otraLista[i][x].getTerreno()) == Agua:
                    if (type(otraLista[i-1][x].getTerreno()) == Tierra and type(otraLista[i+1][x].getTerreno()) == Tierra and type(otraLista[i][x-1].getTerreno()) == Tierra and 
                    type(otraLista[i][x+1].getTerreno()) == Tierra):
                        self.coordenadas[i][x].cambiarTerreno(Tierra(Aire(), None))

    def agregarNaturaleza(self):
        '''Genera en las coordenadas, donde haya tierra, una montana o un arbol'''

        for i in range(0, self.cantCeldasY):
            for x in range(0, self.cantCeldasX):
                if (type(self.coordenadas[i][x].getTerreno()) == Tierra and 
                self.coordenadas[i][x].getNum() in [9, 10]):

                    self.coordenadas[i][x].cambiarNaturaleza(Montana())
                elif (type(self.coordenadas[i][x].getTerreno()) == Tierra  and 
                self.coordenadas[i][x].getNum() in [11, 12, 13, 14, 15, 16, 17]):

                    self.coordenadas[i][x].cambiarNaturaleza(Arbol())

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
    
    def sacarPelado(self, y, x):
        return self.coordenadas[y][x].sacarPelado()

    
    def getPelado(self, y, x):
        return self.coordenadas[y][x].getPelado()


    def zonaInicial(self, y, x):
        '''Muestra la zona donde empieza el personaje'''
        for i in range(1,6):
            self.cambiarVisual(y + i, x, True)
            self.cambiarVisual(y - i, x, True)
            self.cambiarVisual(y, x + i, True)
            self.cambiarVisual(y, x - i, True)

            for e in range(1,6):
                self.cambiarVisual(y + i, x + e, True)
                self.cambiarVisual(y + i, x - e, True)
                self.cambiarVisual(y - i, x + e, True)
                self.cambiarVisual(y - i, x - e, True)
 
    