import pygame, sys, random

pygame.init()
pantalla = pygame.display.set_mode((800,500))

pygame.display.set_caption('Lo barato sale caro lo normal es lo raro')
fps = pygame.time.Clock()

fondo_copado = pygame.Surface((800,500))
fondo_copado.fill((190, 190, 190))
pelado_copado = pygame.image.load('Fotuchas/pelado_copado.png').convert_alpha()
pelado_copado = pygame.transform.scale(pelado_copado, (30, 30))

posa_copado = pygame.image.load('Fotuchas/posa_copado.png').convert_alpha()
posa_copado = pygame.transform.scale(posa_copado, (30, 30))

flor_copada = pygame.image.load('Fotuchas/flor_copada.png').convert_alpha()
flor_copada = pygame.transform.scale(flor_copada, (30, 30))



miLista=[]
for i in range(0,13):
    miLista.append([])
    for x in range(0,20):
        facha = int(random.randrange(0,19))
        miLista[i].append(facha)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pantalla.blit(fondo_copado, (0, 0))
    pos_x=0
    pos_y=0
    for i in range(0, 13):
        for x in range(0, 20):
            if miLista[i][x] == 0:
                pantalla.blit(pelado_copado, (pos_x, pos_y))

            elif miLista[i][x] >= 3 and miLista[i][x] <= 6:            
                pantalla.blit(posa_copado, (pos_x, pos_y))

            else:
                pantalla.blit(flor_copada, (pos_x, pos_y))
            pos_x+=40
        pos_x=0
        pos_y+=40

    pygame.display.update()
    fps.tick(60)