from arquero import Arquero
from celda import  Celda 
import pygame
import random
from arbol import Arbol
from guerrero import Guerrero
from obrero import Obrero
from fundador import Fundador
from tierra import Tierra
from aire import Aire
from agua import Agua
from montana import Montana
from jugador import Jugador
from mina import Mina
from puerto import Puerto
import time
from peludo import Peludo

class Mundo():
    '''El mundo con sus rios, arboles, montanas y pelado'''

    def __init__(self, cantCeldasX, cantCeldasY):
        self.coordenadas = []
        self.cantCeldasX = cantCeldasX
        self.cantCeldasY = cantCeldasY
        self.inicioCeldaX = None
        self.inicioCeldaY = None
        self.crearMundo()
        self.jugador = Jugador()


    def generarTerreno(self):
        '''Completa toda la matriz con agua o tierra'''

        milistaCopada = []

        for i in range(0, self.cantCeldasY):
            milistaCopada.append([])
            for x in range(0, self.cantCeldasX):
                randomN = int(random.randrange(0, 40))

                if randomN in [0, 1, 2, 3, 4, 5, 6]:
                    milistaCopada[i].append(Celda(Agua(Aire(), None), 0, False, randomN))
                else:
                    milistaCopada[i].append(Celda(Tierra(Aire(), None), 0, False, randomN))
        return milistaCopada
    
    def cargadoMapa(self, i, x):
        if self.coordenadas[i][x] == "Tierra":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, False, 0))
        if self.coordenadas[i][x] == "Agua":
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, False, 0))
        if self.coordenadas[i][x] == "Arbol":
            self.coordenadas[i][x] = (Celda(Tierra(Arbol(), None), 0, False, 0))
        if self.coordenadas[i][x] == "Montana":
            self.coordenadas[i][x] = (Celda(Tierra(Montana(), None), 0, False, 0))
        if self.coordenadas[i][x] == "Casa":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerCasa()
        if self.coordenadas[i][x] == "GPersona":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Guerrero())
        if self.coordenadas[i][x] == "OPersona":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Obrero())
        if self.coordenadas[i][x] == "APersona":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Arquero())
        if self.coordenadas[i][x] == "FPersona":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Fundador())
        if self.coordenadas[i][x] == "AGPersona":
            self.inicioCeldaX = x
            self.inicioCeldaY = i
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Guerrero())
        if self.coordenadas[i][x] == "AOPersona":
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Obrero())
        if self.coordenadas[i][x] == "AAPersona":
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Arquero())
        if self.coordenadas[i][x] == "AFPersona":
            self.inicioCeldaX = x
            self.inicioCeldaY = i
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, False, 0))
            self.coordenadas[i][x].ponerPelado(Fundador())
        if self.coordenadas[i][x] == "VTierra":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, True, 0))
        if self.coordenadas[i][x] == "VAgua":
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, True, 0))
        if self.coordenadas[i][x] == "VArbol":
            self.coordenadas[i][x] = (Celda(Tierra(Arbol(), None), 0, True, 0))
        if self.coordenadas[i][x] == "VMontana":
            self.coordenadas[i][x] = (Celda(Tierra(Montana(), None), 0, True, 0))
        if self.coordenadas[i][x] == "VCasa":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerCasa()
        if self.coordenadas[i][x] == "VGPersona":
            self.inicioCeldaX = x
            self.inicioCeldaY = i
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Guerrero())
        if self.coordenadas[i][x] == "VOPersona":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Obrero())
        if self.coordenadas[i][x] == "VAPersona":
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Arquero())
        if self.coordenadas[i][x] == "VFPersona":
            self.inicioCeldaX = x
            self.inicioCeldaY = i
            self.coordenadas[i][x] = (Celda(Tierra(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Fundador())
        if self.coordenadas[i][x] == "VAGPersona":
            self.inicioCeldaX = x
            self.inicioCeldaY = i
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Guerrero())
        if self.coordenadas[i][x] == "VAOPersona":
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Obrero())
        if self.coordenadas[i][x] == "VAAPersona":
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Arquero())
        if self.coordenadas[i][x] == "VAFPersona":
            self.inicioCeldaX = x
            self.inicioCeldaY = i
            self.coordenadas[i][x] = (Celda(Agua(Aire(), None), 0, True, 0))
            self.coordenadas[i][x].ponerPelado(Fundador())
        
            
    
    def cargarMapaG(self): 

        archivo = open("guardado.txt")
        self.coordenadas = []

        for position, line in enumerate(archivo):
            line = line.split(',')
            line.pop()
            self.coordenadas.append(line)

        for i in range(0, (self.cantCeldasY)):
            for x in range(0, (self.cantCeldasX)):
                self.cargadoMapa(i, x)
       
    
    def cargarMapa1(self):
        archivo = open("mapa1.txt")
        self.coordenadas = []
        for position, line in enumerate(archivo):
            line = line.split(',')
            line.pop()
            self.coordenadas.append(line)
        
        for i in range(0, (self.cantCeldasY)):
            for x in range(0, (self.cantCeldasX)):
                self.cargadoMapa(i,x)
        

    def cargarMapa2(self):
        archivo = open("mapa2.txt")
        self.coordenadas = []
        for position, line in enumerate(archivo):
            line = line.split(',')
            line.pop()
            self.coordenadas.append(line)
        
        for i in range(0, (self.cantCeldasY)):
            for x in range(0, (self.cantCeldasX)):
                self.cargadoMapa(i,x)
       

    def modificarMundo(self, listacopada):
        '''Modifica pedazos de agua y tierra'''

        otraLista = listacopada

        for i in range(1, (self.cantCeldasY - 1)):
            for x in range(1, (self.cantCeldasX - 1)):
                if (repr(listacopada[i][x].getTerreno())) == "Tierra":
                    if (repr(listacopada[i - 1][x].getTerreno()) == "Agua" and 
                    (repr(listacopada[i + 1][x].getTerreno())) == "Agua"):

                        otraLista[i][x].cambiarTerreno(Agua(Aire(), None))
                        
                    elif (repr(listacopada[i][x - 1].getTerreno()) == "Agua" and 
                    (repr(listacopada[i][x + 1].getTerreno())) == "Agua"):
                        otraLista[i][x].cambiarTerreno(Agua(Aire(), None))

        self.coordenadas = otraLista

        for i in range(1,(self.cantCeldasY - 1)):
            for x in range(1,(self.cantCeldasX - 1)):
                if (repr(otraLista[i][x].getTerreno())) == "Agua":
                    if (repr(otraLista[i - 1][x].getTerreno()) == "Tierra" and (repr(otraLista[i + 1][x].getTerreno())) == "Tierra" and  (repr(otraLista[i][x - 1].getTerreno())) == "Tierra" and (repr(otraLista[i][x + 1].getTerreno())) == "Tierra"):

                        self.coordenadas[i][x].cambiarTerreno(Tierra(Aire(), None))


    def agregarNaturaleza(self):
        '''Genera en las coordenadas, donde haya tierra, una montana o un arbol'''

        for i in range(0, self.cantCeldasY):
            for x in range(0, self.cantCeldasX):
                if (repr(self.coordenadas[i][x].getTerreno()) == "Tierra" and 
                self.coordenadas[i][x].getNum() in [9, 10]):
                    self.coordenadas[i][x].cambiarNaturaleza(Montana())

                elif (repr((self.coordenadas[i][x].getTerreno())) == "Tierra" and 
                self.coordenadas[i][x].getNum() in [11, 12, 13, 14, 15, 16, 17]):
                    self.coordenadas[i][x].cambiarNaturaleza(Arbol())


    def contarPelados(self):
        cont = 0
        for i in range(0, self.cantCeldasY):
            for x in range(0, self.cantCeldasX):
                if (self.coordenadas[i][x].getPelado()) == True and (repr(self.getClasePersona(i, x))) != "Peludo":
                    cont += 1
        return cont


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
    
    def ponerPelado(self, y, x, clase):
        return self.coordenadas[y][x].ponerPelado(clase)

    def ponerPelado(self, y, x, clase):
        return self.coordenadas[y][x].ponerPelado(clase)
    
    def ponerMarcador(self, y, x, nuevoOrden):
        return self.coordenadas[y][x].ponerMarcador(nuevoOrden)

    def sacarPelado(self, y, x):
        return self.coordenadas[y][x].sacarPelado()
    
    def cambiarClasePersona(self, y, x, clase):
        return self.coordenadas[y][x].cambiarClasePersona(clase)
    
    def getClasePersona(self, y, x):
        return self.coordenadas[y][x].getClasePersona()

    def sacarMarcador(self, y, x):
        return self.coordenadas[y][x].sacarMarcador()

    def getPelado(self, y, x):
        return self.coordenadas[y][x].getPelado()

    def getMarcador(self, y, x):
        return self.coordenadas[y][x].getMarcador()

    def getCasa(self, y, x):
        return self.coordenadas[y][x].getCasa()

    def getPeludoCasa(self, y, x):
        return self.coordenadas[y][x].getPeludoCasa()

    def ponerCasa(self, y, x):
        return self.coordenadas[y][x].ponerCasa()

    def ponerPeludoCasa(self, y, x):
        return self.coordenadas[y][x].ponerPeludoCasa()

    def ponerMina(self, y, x):
        return self.coordenadas[y][x].ponerMina()

    def ponerPuerto(self, y, x):
        return self.coordenadas[y][x].ponerPuerto()

    def getMina(self, y, x):
        return self.coordenadas[y][x].getMina()

    def getPuerto(self, y, x):
        return self.coordenadas[y][x].getPuerto()
    
    def getCorral(self, y, x):
        return self.coordenadas[y][x].getCorral()

    def getCultivo(self, y, x):
        return self.coordenadas[y][x].getCultivo()

    def ponerCorral(self, y, x):
        return self.coordenadas[y][x].ponerCorral()

    def ponerCultivo(self, y, x):
        return self.coordenadas[y][x].ponerCultivo()

    def getOrdenMarcador(self, y, x):
        return self.coordenadas[y][x].getOrdenMarcador()

    def getInicioX(self):
        return self.inicioCeldaX
    
    def getInicioY(self):
        return self.inicioCeldaY

    def zonaInicial(self, y, x):
        '''Muestra la zona donde empieza el personaje'''
        self.ponerCivJugador(y, x)
        for i in range(1, 6):
            self.cambiarVisual(y + i, x, True)
            self.ponerCivJugador(y + i, x)
            self.cambiarVisual(y - i, x, True)
            self.ponerCivJugador(y - i, x)
            self.cambiarVisual(y, x + i, True)
            self.ponerCivJugador(y, x + i)
            self.cambiarVisual(y, x - i, True)
            self.ponerCivJugador(y, x - i)
            for e in range(1, 6):
                self.cambiarVisual(y + i, x + e, True)
                self.ponerCivJugador(y + i, x + e)
                self.cambiarVisual(y + i, x - e, True)
                self.ponerCivJugador(y + i, x - e)
                self.cambiarVisual(y - i, x + e, True)
                self.ponerCivJugador(y - i, x + e)
                self.cambiarVisual(y - i, x - e, True)
                self.ponerCivJugador(y - i, x - e)
                
                
    def zonaInicialPeludo(self):
        civPrimera = [10, 170]
        civSegunda = [90, 70]
        civTercera = [90, 170]
        for i in range(1,4):
            if i == 1:
                y = civPrimera[0]
                x = civPrimera[1]
            elif i == 2:
                y = civSegunda[0]
                x = civSegunda[1]
            else:
                y = civTercera[0]
                x = civTercera[1]
            self.ponerCivPeludo(y, x, i + 1)
            for l in range(1, 6):
                self.ponerCivPeludo(y + l, x, i + 1)
                self.ponerCivPeludo(y - l, x, i + 1)
                self.ponerCivPeludo(y, x + l, i + 1)
                self.ponerCivPeludo(y, x - l, i + 1)
                for h in range(1, 6):
                    self.ponerCivPeludo(y + l, x + h, i + 1)
                    self.ponerCivPeludo(y + l, x - h, i + 1)
                    self.ponerCivPeludo(y - l, x + h, i + 1)
                    self.ponerCivPeludo(y - l, x - h, i + 1)
            for z in range(1, 4):
                self.coordenadas[y][x + z].cambiarTerreno(Tierra(Aire(), None))
                self.ponerPeludoCasa(y, x + z)
                self.ponerPelado(y, x + z, Peludo())
            


    def colocarCivilizacion(self, y, x):
        self.sacarPelado(y, x)
        for i in range(1,4):
            
            casaX = int(random.randrange(1, 4))
            casaY = int(random.randrange(1, 4))
            if i == 1:
                while casaX != 999:
                    if (repr(self.getTerreno(y + casaY, x + casaX)) == "Tierra" and
                    repr(self.getNaturaleza(y + casaY, x + casaX)) == "Aire" and 
                    self.getCasa(y + casaY, x + casaX) == None):

                        self.ponerCasa(y + casaY, x + casaX)
                        self.ponerPelado(y + casaY, x + casaX, Guerrero())
                        
                        
                        casaX = 999
                    else:
                        casaX = int(random.randrange(1, 4))
                        casaY = int(random.randrange(1, 4))
            elif i == 2:
                while casaX != 999:
                    if (repr(self.getTerreno(y - casaY, x - casaX)) == "Tierra" and
                    repr(self.getNaturaleza(y - casaY, x - casaX)) == "Aire" and 
                    self.getCasa(y - casaY, x - casaX) == None):
                        self.ponerCasa(y - casaY, x - casaX)
                        self.ponerPelado(y - casaY, x - casaX, Obrero())
                        
                        casaX = 999
                    else:
                        casaX = int(random.randrange(1, 4))
                        casaY = int(random.randrange(1, 4))
            else:
                while casaX != 999:
                    if (repr(self.getTerreno(y - casaY, x + casaX)) == "Tierra" and
                    repr(self.getNaturaleza(y - casaY, x + casaX)) == "Aire" and 
                    self.getCasa(y - casaY, x + casaX) == None):
                        self.ponerCasa(y - casaY, x + casaX)
                        self.ponerPelado(y - casaY, x + casaX, Arquero())
                        
                        casaX = 999
                    else:
                        casaX = int(random.randrange(1, 4))
                        casaY = int(random.randrange(1, 4))
                

    def cambiarVisualMov(self, visualInicioY, visualInicioX, visualMov):
        self.cambiarVisual(visualInicioY, visualInicioX, True)
        self.cambiarVisual(visualInicioY, (visualInicioX + 1), True)
        self.cambiarVisual(visualInicioY, (visualInicioX - 1), True)
        self.cambiarVisual(visualInicioY + 1, (visualInicioX + 1), True)
        self.cambiarVisual(visualInicioY - 1, (visualInicioX - 1), True)
        self.cambiarVisual(visualInicioY - 1, (visualInicioX + 1), True)
        self.cambiarVisual(visualInicioY + 1, (visualInicioX - 1), True)
        self.cambiarVisual(visualInicioY + 1, (visualInicioX), True)
        self.cambiarVisual(visualInicioY - 1, (visualInicioX), True)

        if visualMov == True:
            self.ponerCivJugador(visualInicioY, visualInicioX)
            self.ponerCivJugador(visualInicioY, (visualInicioX + 1))
            self.ponerCivJugador(visualInicioY, (visualInicioX - 1))
            self.ponerCivJugador(visualInicioY + 1, (visualInicioX + 1))
            self.ponerCivJugador(visualInicioY - 1, (visualInicioX - 1))
            self.ponerCivJugador(visualInicioY - 1, (visualInicioX + 1))
            self.ponerCivJugador(visualInicioY + 1, (visualInicioX - 1))
            self.ponerCivJugador(visualInicioY + 1, (visualInicioX))
            self.ponerCivJugador(visualInicioY - 1, (visualInicioX))


    def movimientoCivPeludo(self, y, x, civ):
        self.ponerCivPeludo(y, x + 1, civ)
        self.ponerCivPeludo(y, x - 1, civ)
        self.ponerCivPeludo(y + 1, x, civ)
        self.ponerCivPeludo(y - 1, x, civ)
        self.ponerCivPeludo(y + 1, x + 1, civ)
        self.ponerCivPeludo(y + 1, x - 1, civ)
        self.ponerCivPeludo(y - 1, x + 1, civ)
        self.ponerCivPeludo(y - 1, x - 1, civ)
        self.ponerCivPeludo(y, x, civ)


    def movimientoPeludo(self, y, x, civ):
        eje = int(random.randrange(1, 5))
        ejeXDistancia = int(random.randrange(0, 13))
        ejeYDistancia = int(random.randrange(0, 13))


    def sacarArbol(self, y, x):
        self.coordenadas[y][x].sacarArbol()
    
    def cantidadMaterial(self, y, x):
        return self.coordenadas[y][x].randomMaterial()

    def tipoBorde(self, y, x):
        if self.coordenadas[y][x].getCivilizacion() != 0:
            if self.coordenadas[y][x].getCivilizacion() == 1:
                if (self.coordenadas[y-1][x].getCivilizacion() != 1 and self.coordenadas[y][x+1].getCivilizacion() != 1 and 
                    self.coordenadas[y+1][x].getCivilizacion() == 1 and self.coordenadas[y][x-1].getCivilizacion() == 1):
                    return "borde_arriba_derecha"
                elif (self.coordenadas[y-1][x].getCivilizacion() != 1 and self.coordenadas[y][x-1].getCivilizacion() != 1 and 
                    self.coordenadas[y+1][x].getCivilizacion() == 1 and self.coordenadas[y][x+1].getCivilizacion() == 1):
                    return "borde_arriba_izquierda"
                elif (self.coordenadas[y+1][x].getCivilizacion() != 1 and self.coordenadas[y][x-1].getCivilizacion() != 1 and 
                    self.coordenadas[y-1][x].getCivilizacion() == 1 and self.coordenadas[y][x+1].getCivilizacion() == 1):
                    return "borde_abajo_izquierda"
                elif (self.coordenadas[y+1][x].getCivilizacion() != 1 and self.coordenadas[y][x+1].getCivilizacion() != 1 and 
                    self.coordenadas[y-1][x].getCivilizacion() == 1 and self.coordenadas[y][x-1].getCivilizacion() == 1):
                    return "borde_abajo_derecha"
                elif (self.coordenadas[y+1][x].getCivilizacion() != 1 and self.coordenadas[y][x+1].getCivilizacion() == 1 and 
                    self.coordenadas[y-1][x].getCivilizacion() == 1 and self.coordenadas[y][x-1].getCivilizacion() == 1):
                    return "borde_abajo"
                elif (self.coordenadas[y+1][x].getCivilizacion() == 1 and self.coordenadas[y][x+1].getCivilizacion() == 1 and 
                    self.coordenadas[y-1][x].getCivilizacion() != 1 and self.coordenadas[y][x-1].getCivilizacion() == 1):
                    return "borde_arriba"
                elif (self.coordenadas[y+1][x].getCivilizacion() == 1 and self.coordenadas[y][x+1].getCivilizacion() != 1 and 
                    self.coordenadas[y-1][x].getCivilizacion() == 1 and self.coordenadas[y][x-1].getCivilizacion() == 1):
                    return "borde_derecha"
                elif (self.coordenadas[y+1][x].getCivilizacion() == 1 and self.coordenadas[y][x+1].getCivilizacion() == 1 and
                    self.coordenadas[y-1][x].getCivilizacion() == 1 and self.coordenadas[y][x-1].getCivilizacion() != 1):
                    return "borde_izquierda"
            else:
                civPeludo = self.coordenadas[y][x].getCivilizacion()
                if (self.coordenadas[y-1][x].getCivilizacion() != civPeludo and self.coordenadas[y][x+1].getCivilizacion() != civPeludo and 
                    self.coordenadas[y+1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x-1].getCivilizacion() == civPeludo):
                    return "pel_borde_arriba_derecha"
                elif (self.coordenadas[y-1][x].getCivilizacion() != civPeludo and self.coordenadas[y][x-1].getCivilizacion() != civPeludo and 
                    self.coordenadas[y+1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x+1].getCivilizacion() == civPeludo):
                    return "pel_borde_arriba_izquierda"
                elif (self.coordenadas[y+1][x].getCivilizacion() != civPeludo and self.coordenadas[y][x-1].getCivilizacion() != civPeludo and 
                    self.coordenadas[y-1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x+1].getCivilizacion() == civPeludo):
                    return "pel_borde_abajo_izquierda"
                elif (self.coordenadas[y+1][x].getCivilizacion() != civPeludo and self.coordenadas[y][x+1].getCivilizacion() != civPeludo and 
                    self.coordenadas[y-1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x-1].getCivilizacion() == civPeludo):
                    return "pel_borde_abajo_derecha"
                elif (self.coordenadas[y+1][x].getCivilizacion() != civPeludo and self.coordenadas[y][x+1].getCivilizacion() == civPeludo and 
                    self.coordenadas[y-1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x-1].getCivilizacion() == civPeludo):
                    return "pel_borde_abajo"
                elif (self.coordenadas[y+1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x+1].getCivilizacion() == civPeludo and 
                    self.coordenadas[y-1][x].getCivilizacion() != civPeludo and self.coordenadas[y][x-1].getCivilizacion() == civPeludo):
                    return "pel_borde_arriba"
                elif (self.coordenadas[y+1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x+1].getCivilizacion() != civPeludo and 
                    self.coordenadas[y-1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x-1].getCivilizacion() == civPeludo):
                    return "pel_borde_derecha"
                elif (self.coordenadas[y+1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x+1].getCivilizacion() == civPeludo and 
                    self.coordenadas[y-1][x].getCivilizacion() == civPeludo and self.coordenadas[y][x-1].getCivilizacion() != civPeludo):
                    return "pel_borde_izquierda"
        

    def cantidadMaterialCultivo(self, y, x):
        return self.coordenadas[y][x].randomMaterialCultivo()

    def cantidadMaterialCorral(self, y, x):
        return self.coordenadas[y][x].randomMaterialCorral()
    
    def agregarMadera(self, cant):
        self.jugador.agregarMadera(cant)
    
    def restarMadera(self, cant):
        self.jugador.restarMadera(cant)
    
    def agregarPiedra(self, cant):
        self.jugador.agregarPiedra(cant)
    
    def agregarComida(self, cant):
        self.jugador.agregarComida(cant)

    def restarPiedra(self, cant):
        self.jugador.restarPiedra(cant)
    
    def getMadera(self):
        self.jugador.getMadera()
    
    def getEnergia(self):
        return self.jugador.getEnergia()
    
    def getMadera(self):
        return self.jugador.getMadera()
    
    def getPiedra(self):
        return self.jugador.getPiedra()
    
    def getComida(self):
        return self.jugador.getComida()

    def restarEnergia(self, cant):
        self.jugador.restarEnergia(cant)

    def restarComida(self, cant):
        self.jugador.restarComida(cant)

    def setEnergia(self):
        self.jugador.setEnergia()
    
    def setComida(self):
        self.jugador.setComida()
        
    def hacerBarco(self):
        self.jugador.crearBarco()
    
    def getBarco(self):
        return self.jugador.getBarco()
    
    def restarUsoBarco(self):
        self.jugador.restarUsoBarco()
    
    def getUsosBarco(self):
        return self.jugador.getUsosBarco()
    
    def hacerCasa(self):
        self.jugador.hacerCasa()
    
    def getFundadorActivo(self):
        return self.jugador.getFundadorActivo()
    
    def getGuerrerorActivo(self):
        return self.jugador.getGuerrerorActivo()
    
    def getArqueroActivo(self):
        return self.jugador.getArqueroActivo()
    
    def getObreroActivo(self):
        return self.jugador.getObreroActivo()
    
    def ponerCivJugador(self, y, x):
        self.coordenadas[y][x].ponerJugadorCiv()

    def ponerCivPeludo(self, y, x, civ):
        self.coordenadas[y][x].ponerPeludoCiv(civ)

    def matarFundador(self):
        self.jugador.matarFundador()
    
    def chequearClase(self, y, x):
        if (repr(self.getClasePersona(y, x))) == "Guerrero":                          
            clase = "Guerrero"

        elif (repr(self.getClasePersona(y, x))) == "Arquero":
            clase = "Arquero"
        
        elif (repr(self.getClasePersona(y, x))) == "Obrero":
            clase = "Obrero"
        
        return clase

    def hacerPuerto(self):
        self.jugador.hacerPuerto()
    
    def getConstruccion(self, y, x):
        return self.coordenadas[y][x].getConstruccion()

    def hacerCorral(self):
        self.jugador.hacerCorral()

    def hacerCultivo(self):
        self.jugador.hacerCultivo()

    def hacerMina(self):
        self.jugador.hacerMina()
    
    def getTurno(self):
        return self.jugador.getTurno()

    def setTurno(self):
        self.jugador.setTurno()
    
    def getCantTurno(self):
        return self.jugador.getCantTurno()
    
    def reiniciarTurnos(self):
        self.jugador.reiniciarTurno()