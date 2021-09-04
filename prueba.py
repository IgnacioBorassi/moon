import pygame, sys
import random

from pygame.constants import MIDIIN
from mundo import Mundo
from arbol import Arbol
from tierra import Tierra
from montana import Montana
pygame.init()

pantalla = pygame.display.set_mode((1080,520))

pygame.display.set_caption('Lo barato sale caro lo normal es lo raro estare sonado me visto despacio si estoy apurado amo ser odiado y tener la facha de un repetidor y la anota de un aprobado')
fps = pygame.time.Clock()


fondo_copado = pygame.Surface((1080,520))
fondo_copado.fill((190, 190, 190))

escalaX = 40
escalaY = 40

celdasX = 216
celdasY = 104

pasto_fond = pygame.image.load('Fotuchas/pasto.png').convert_alpha()
pasto_fond = pygame.transform.scale(pasto_fond, (40,40))
pasto_rect = pasto_fond.get_rect(topleft = (0,0))


montaña_sup = pygame.image.load('Fotuchas/montana.png').convert_alpha()
montaña_sup = pygame.transform.scale(montaña_sup, (escalaX, escalaY))
montaña_rect = montaña_sup.get_rect(topleft = (100,100))

posX=0
posY=0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
                
    pantalla.blit(fondo_copado, (0, 0))
    for i in range(0,14):
        for x in range(0,40):

            pantalla.blit(pasto_fond, (posX,posY))
            posX+=40
    posY+=40


    pygame.display.update()
    fps.tick(60)