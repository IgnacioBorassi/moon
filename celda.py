import pygame
from persona import Persona
from marcador import Marcador
from casa import Casa
from puerto import Puerto
from mina import Mina
from corral import Corral
from cultivo import Cultivo
from peludocasa import PeludoCasa

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
        self.peludoCasa = PeludoCasa(None)
        self.puerto = Puerto(None)
        self.mina = Mina(None)
        self.corral = Corral(None)
        self.cultivo = Cultivo(None)
        
    
    def visualizar(self, visual):
        '''Permite ver o no ver la celda'''
        self.visual = visual

    def cambiarCivilizacion(self, nuevaCiv):
        '''Permite cambiar la propiedad de una celda'''
        self.propiedad = nuevaCiv

    def ponerPeludoCiv(self, nuevaCiv):
        self.cambiarCivilizacion(nuevaCiv)

    def ponerJugadorCiv(self):
        self.cambiarCivilizacion(1)

    def getCivilizacion(self):
        return self.propiedad

    def getTerreno(self):
        return self.terreno

    def getNum(self):
        return self.numero
        
    def getMarcador(self):
        return self.marcador.getMarcador()
    
    def getConstruccion(self):
        return self.terreno.getConstruccion()

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

    def ponerPeludo(self, clase):
        self.persona.ponerPeludo(clase)

    def sacarPelado(self):
        self.persona.sacarPelado()

    def getPelado(self):
        return self.persona.getPersona()

    def ponerCasa(self):
        self.terreno.setConstruccion()
        self.casa.ponerCasa()

    def ponerPeludoCasa(self):
        '''Pone la casa del Peludo y marca la celda como construida'''
        self.terreno.setConstruccion()
        self.peludoCasa.ponerPeludoCasa()
    
    def getCasa(self):
        return self.casa.getCasa()

    def getPeludoCasa(self):
        return self.peludoCasa.getPeludoCasa()

    def getPuerto(self):
        return self.puerto.getPuerto()
    
    def getCorral(self):
        return self.corral.getCorral()

    def getCultivo(self):
        return self.cultivo.getCultivo()
        
    def ponerPuerto(self):
        '''Pone un puerto y marca la celda como construida'''
        self.terreno.setConstruccion()
        self.puerto.ponerPuerto()

    def ponerCorral(self):
        '''Pone un corral y marca la celda como construida'''
        self.terreno.setConstruccion()
        self.corral.ponerCorral()

    def ponerCultivo(self):
        '''Pone un cultivo y marca la celda como construida'''
        self.terreno.setConstruccion()
        self.cultivo.ponerCultivo()

    def getMina(self):
        return self.mina.getMina()
    
    def ponerMina(self):
        '''Pone una mina y marca la celda como construida'''
        self.terreno.setConstruccion()
        self.mina.ponerMina()

    def getOrdenMarcador(self):
        return self.marcador.getOrdenMarcador()

    def sacarArbol(self):
        self.terreno.sacarArbol()

    def randomMaterial(self):
        return self.terreno.randomMaterial()
    
    def randomMaterialCorral(self):
        return self.corral.randomMaterial()
    
    def randomMaterialCultivo(self):
        return self.cultivo.randomMaterial()

    def cambiarClasePersona(self, clase):
        self.persona.cambiarClase(clase)

    def getClasePersona(self):
        return self.persona.getClase()