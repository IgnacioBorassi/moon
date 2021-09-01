import pygame, sys
import random

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

class porqueria:
    def __init__(self, tipo, mugre, numero):
        self.tipo = tipo
        self.mugre = mugre
        self.numero = numero

miListaHumilde=[]
miLista=[]
milistaCopada=[]
randomN = 0

for i in range(0,celdasY):
    miLista.append([])
    miListaHumilde.append([])
    milistaCopada.append([])
    for x in range(0,celdasX):
        randomN = int(random.randrange(0,40))
        if randomN in [0,1,2,3,4,5,6]:
            miLista[i].append(porqueria("Agua", "Aire", randomN))
            miListaHumilde[i].append(porqueria("Agua", "Aire", randomN))
            milistaCopada[i].append(porqueria("Agua", "Aire", randomN))
        else:
            miLista[i].append(porqueria("Tierra", "Aire", randomN))
            miListaHumilde[i].append(porqueria("Tierra", "Aire", randomN))
            milistaCopada[i].append(porqueria("Tierra", "Aire", randomN))

for i in range(1,(celdasY - 1)):
    for x in range(1, (celdasX - 1)):
        if miListaHumilde[i][x].tipo == "Tierra":
            if miListaHumilde[i-1][x].tipo == "Agua" and miListaHumilde[i+1][x].tipo == "Agua":
                milistaCopada[i][x].tipo = "Agua"
                miLista[i][x].tipo = "Agua"
                
            elif miListaHumilde[i][x-1].tipo == "Agua" and miListaHumilde[i][x+1].tipo == "Agua":
                milistaCopada[i][x].tipo = "Agua"
                miLista[i][x].tipo = "Agua"


for i in range(1,(celdasY - 1)):
    for x in range(1,(celdasX - 1)):
        if milistaCopada[i][x].tipo == "Agua":
            if milistaCopada[i-1][x].tipo == "Tierra" and milistaCopada[i+1][x].tipo == "Tierra" and milistaCopada[i][x-1].tipo == "Tierra" and milistaCopada[i][x+1].tipo == "Tierra":
                miLista[i][x].tipo = "Tierra"
            



for i in range(0,celdasY):
    for x in range(0,celdasX):
        if miLista[i][x].tipo == "Tierra" and miLista[i][x].numero in [9, 10]:
            miLista[i][x].mugre = "Montana"
        elif miLista[i][x].tipo == "Tierra" and miLista[i][x].numero in [11, 12, 13, 14, 15, 16, 17]:
            miLista[i][x].mugre = "Arbol"

inicioCeldaY = 0
inicioCeldaX = 0
pos_x =  0
hola = 10

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
                
            if event.key == pygame.K_KP_1:
                hola = 0

            if event.key == pygame.K_KP_2:
                hola = 1

            if event.key == pygame.K_KP_3:
                hola = 2


    pantalla.blit(fondo_copado, (0, 0))
    
    if hola == 2:
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
    elif hola == 1:
        for i in range(0, celdasY):
            for x in range(0, celdasX):
                if milistaCopada[i][x].tipo == "Tierra":
                    pantalla.blit(pasto_fond, (pos_x, pos_y))
                    
                    if milistaCopada[i][x].mugre == "Arbol":
                        pantalla.blit(arbol_sup, (pos_x, pos_y))
                    elif milistaCopada[i][x].mugre == "Montana":
                        pantalla.blit(montaña_sup, (pos_x, pos_y))
                    
                else:
                    pantalla.blit(agua_fond, (pos_x, pos_y))

                pos_x+=escalaX
            pos_x=inicioCeldaX
            pos_y+=escalaY
    elif hola == 0:
        for i in range(0, celdasY):
            for x in range(0, celdasX):
                if miListaHumilde[i][x].tipo == "Tierra":
                    pantalla.blit(pasto_fond, (pos_x, pos_y))
                    
                    if miListaHumilde[i][x].mugre == "Arbol":
                        pantalla.blit(arbol_sup, (pos_x, pos_y))
                    elif miListaHumilde[i][x].mugre == "Montana":
                        pantalla.blit(montaña_sup, (pos_x, pos_y))
                    
                else:
                    pantalla.blit(agua_fond, (pos_x, pos_y))

                pos_x+=escalaX
            pos_x=inicioCeldaX
            pos_y+=escalaY

    pantalla.blit(pelado_sup, (520, 240))


    pygame.display.update()
    fps.tick(60)