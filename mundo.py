from celda import  Celda 
import pygame
import random

class Mundo():
    def __init__(self, cantCeldasX, cantCeldasY):
        self.coordenadas = []
        self.cantCeldasX = cantCeldasX
        self.cantCeldasY = cantCeldasY
        self.crearMundo()

    def generarTerreno(self):
        milistaCopada = []

        for i in range(0, self.cantCeldasY):
            milistaCopada.append([])
            for x in range(0, self.cantCeldasX):
                randomN = int(random.randrange(0,40))
                if randomN in [0,1,2,3,4,5,6]:
                    milistaCopada[i].append(Celda("Agua", "Aire", "Nada", "Nadie", "Negro", randomN))
                else:
                    milistaCopada[i].append(Celda("Tierra", "Aire", "Nada", "Nadie", "Negro", randomN))
        
        return milistaCopada

    def modificarMundo(self, listacopada):

        otraLista = listacopada

        for i in range(1, (self.cantCeldasY - 1)):
            for x in range(1, (self.cantCeldasX - 1)):
                if listacopada[i][x].getTerreno() == "Tierra":
                    if listacopada[i-1][x].getTerreno() == "Agua" and listacopada[i+1][x].getTerreno() == "Agua":
                        otraLista[i][x].cambiarTerreno("Agua")
                        
                    elif listacopada[i][x-1].getTerreno() == "Agua" and listacopada[i][x+1].getTerreno() == "Agua":
                        otraLista[i][x].cambiarTerreno("Agua")

        self.coordenadas = otraLista

        for i in range(1,(self.cantCeldasY - 1)):
            for x in range(1,(self.cantCeldasX - 1)):
                if otraLista[i][x].tipo == "Agua":
                    if otraLista[i-1][x].getTerreno() == "Tierra" and otraLista[i+1][x].getTerreno() == "Tierra" and  otraLista[i][x-1].getTerreno() == "Tierra" and otraLista[i][x+1].getTerreno() == "Tierra":
                        self.coordenadas[i][x].cambiarTerreno("Tierra")

    def agregarNaturaleza(self):
        
        for i in range(0, self.cantCeldasY):
            for x in range(0, self.cantCeldasX):
                if self.coordenadas[i][x].getTerreno() == "Tierra" and self.coordenadas[i][x].getNum() in [9, 10]:
                    self.coordenadas[i][x].agregarNat("Montana")
                elif self.coordenadas[i][x].getTerreno() == "Tierra" and self.coordenadas[i][x].getNum() in [11, 12, 13, 14, 15, 16, 17]:
                    self.coordenadas[i][x].agregarNat("Arbol")

    def crearMundo(self):
        self.modificarMundo(self.generarTerreno())
        self.agregarNaturaleza()

    def getTerreno(self, x, y):
        return self.coordenadas[y][x].getTerreno()

