import pygame
from persona import Persona
from marcador import Marcador
from casa import Casa
from puerto import Puerto
from mina import Mina
class Celda():
    '''Clase Celda contiene el terreno, el propietario, visual y un numero'''

    def __init__(self, terreno, propiedad, visual, num):
        self.terreno = terreno
        self.propiedad = propiedad
        self.visual = visual
        self.numero = num
        self.persona = Persona(None)
        self.marcador = Marcador(None)
        self.casa = Casa(None)
        self.puerto = Puerto(None)
        self.mina = Mina(None)
        

    def tomarTerreno(self, propiedad):
        self.propiedad = propiedad
    
    def visualizar(self, visual):
        '''Permite ver o no ver la celda'''
        self.visual = visual

    def getTerreno(self):
        return self.terreno

    def getNum(self):
        return self.numero
        
    def getMarcador(self):
        return self.marcador.getMarcador()
    
    def getConstruccion(self):
        self.terreno.getConstruccion()

    def ponerMarcador(self, nuevoOrden):
        self.marcador.ponerMarcador(nuevoOrden)

    def sacarMarcador(self):
        self.marcador.sacarMarcador()

    def cambiarTerreno(self, nuevoTerreno):
        '''Cambia el terreno entre tierra y agua'''
        self.terreno = nuevoTerreno

    def cambiarNaturaleza(self, nuevaNaturaleza):
        '''Cambia la celda entre arbol y montana'''
        self.terreno.cambiarNaturaleza(nuevaNaturaleza)  
    
    def getNaturaleza(self):
        return self.terreno.getNaturaleza()

    def getVisual(self):
        return self.visual
    
    def cambiarVisual(self, nuevoVisual):
        '''Cambia la celda para poder visualizarla'''
        self.visual = nuevoVisual

    def ponerPelado(self, clase):
        self.persona.ponerPelado(clase)

    def sacarPelado(self):
        self.persona.sacarPelado()

    def getPelado(self):
        return self.persona.getPersona()

    def ponerCasa(self):
        self.casa.ponerCasa()
    
    def getCasa(self):
        return self.casa.getCasa()

    def getPuerto(self):
        return self.puerto.getPuerto()
    
    def ponerPuerto(self):
        self.puerto.ponerPuerto()

    def getMina(self):
        return self.mina.getMina()
    
    def ponerMina(self):
        self.mina.ponerMina()

    def getOrdenMarcador(self):
        return self.marcador.getOrdenMarcador()

    def sacarArbol(self):
        self.terreno.sacarArbol()

    def randomMaterial(self):
        return self.terreno.randomMaterial()
    
    def cambiarClasePersona(self, clase):
        self.persona.cambiarClase(clase)

    def getClasePersona(self):
        return self.persona.getClase()