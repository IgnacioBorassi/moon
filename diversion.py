import pygame, sys
import random
from mundo import Mundo

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

montaña_sup = pygame.image.load('Fotuchas/montana.png').convert_alpha()
montaña_sup = pygame.transform.scale(montaña_sup, (escalaX, escalaY))

agua_fond = pygame.image.load('Fotuchas/agua.png').convert_alpha()
agua_fond = pygame.transform.scale(agua_fond, (escalaX, escalaY))

pasto_fond = pygame.image.load('Fotuchas/pasto.png').convert_alpha()
pasto_fond = pygame.transform.scale(pasto_fond, (escalaX, escalaY))

arbol_sup = pygame.image.load('Fotuchas/arbol.png').convert_alpha()
arbol_sup = pygame.transform.scale(arbol_sup, (escalaX, escalaY))

pelado_sup = pygame.image.load('Fotuchas/pelado.png').convert_alpha()
pelado_sup = pygame.transform.scale(pelado_sup, (escalaX, escalaY))



inicioCeldaY = 0
inicioCeldaX = 0
pos_x =  0
hola = 10
mundo = Mundo()

mundo.getTerreno(i,x)

while True:

    pos_y=inicioCeldaY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                inicioCeldaY -= escalaY
            
            if event.key == pygame.K_UP:
                inicioCeldaY += escalaY
            
            if event.key == pygame.K_RIGHT:
                inicioCeldaX -= escalaX

            if event.key == pygame.K_LEFT:
                inicioCeldaX += escalaX
                
    pantalla.blit(fondo_copado, (0, 0))
    
    for i in range(0, celdasY):
        for x in range(0, celdasX):
            if miLista[i][x].tipo == "Tierra":
                pantalla.blit(pasto_fond, (pos_x, pos_y))
                
                if miLista[i][x].mugre == "Arbol":
                    pantalla.blit(arbol_sup, (pos_x, pos_y))
                elif miLista[i][x].mugre == "Montana":
                    pantalla.blit(montaña_sup, (pos_x, pos_y))
                
            else:
                pantalla.blit(agua_fond, (pos_x, pos_y))

            pos_x+=escalaX
        pos_x=inicioCeldaX
        pos_y+=escalaY


    pantalla.blit(pelado_sup, (520, 240))


    pygame.display.update()
    fps.tick(60)