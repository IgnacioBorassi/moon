from pygame.cursors import tri_right
from aire import Aire
import pygame, sys, random
from mundo import Mundo
from arbol import Arbol
from tierra import Tierra
from montana import Montana
from menu import Menu
<<<<<<< HEAD
from persona import Persona
=======
from marcador import Marcador
>>>>>>> 1957675adf06ff9027a245c52f24127357a59c13
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

negro_fond = pygame.image.load('Fotuchas/negro.png').convert_alpha()
negro_fond = pygame.transform.scale(negro_fond, (escalaX, escalaY))

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
sizeX = 216
sizeY = 104
mundo = Mundo(sizeX, sizeY)
menu = Menu()

visualInicioY = int(random.randrange(20,80))
visualInicioX = int(random.randrange(20,190))
while (type(mundo.getTerreno(visualInicioY, visualInicioX)) != Tierra or type(mundo.getNaturaleza(visualInicioY, visualInicioX)) != Aire):
    visualInicioY = int(random.randrange(20,80))
    visualInicioX = int(random.randrange(20,190))

for i in range(1,6):
    mundo.cambiarVisual(visualInicioY+i, visualInicioX, True)
    mundo.cambiarVisual(visualInicioY-i, visualInicioX, True)
    mundo.cambiarVisual(visualInicioY, visualInicioX+i, True)
    mundo.cambiarVisual(visualInicioY, visualInicioX-i, True)

    for x in range(1,6):
        mundo.cambiarVisual(visualInicioY+i, visualInicioX+x, True)
        mundo.cambiarVisual(visualInicioY+i, visualInicioX-x, True)
        mundo.cambiarVisual(visualInicioY-i, visualInicioX+x, True)
        mundo.cambiarVisual(visualInicioY-i, visualInicioX-x, True)

mundo.cambiarVisual(visualInicioY, visualInicioX, True)
mundo.ponerPelado(visualInicioY, visualInicioX)
inicioCeldaY = (visualInicioY * -40) + 40*6
inicioCeldaX = (visualInicioX * -40) + 40*13


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.getStartRect().collidepoint(event.pos):
                menu.apagarMenu()
            elif menu.getExitRect().collidepoint(event.pos):
                pygame.quit()
                exit()

        if event.type == pygame.KEYDOWN:
            
            
            
            if event.key == pygame.K_ESCAPE:
                
                menu.prenderMenu()
            if menu.getActivo() == False:
                if event.key == pygame.K_j:
                    inicioCeldaY = (visualInicioY * -40) + 40*6
                    inicioCeldaX = (visualInicioX * -40) + 40*13

                if event.key == pygame.K_DOWN:
                    inicioCeldaY -= escalaY
                    if inicioCeldaY < -3640:
                        inicioCeldaY = -3640
                
                    print("Eje Y Lista: "+str(inicioCeldaY))
                    print("Eje X Lista: "+str(inicioCeldaX))
                
                if event.key == pygame.K_s:
                    mundo.sacarPelado(visualInicioY, visualInicioX)
                    visualInicioY +=1
                    if visualInicioY > 101:
                        visualInicioY = 101
                    if (type(mundo.getTerreno(visualInicioY, visualInicioX)) == Tierra 
                    and type(mundo.getNaturaleza(visualInicioY, visualInicioX)) == Aire):
                        print(type(mundo.getTerreno(visualInicioY,visualInicioX)))
                        mundo.ponerPelado(visualInicioY, visualInicioX)
                        mundo.cambiarVisual(visualInicioY, visualInicioX, True)
                        mundo.cambiarVisual(visualInicioY, (visualInicioX + 1), True)
                        mundo.cambiarVisual(visualInicioY, (visualInicioX - 1), True)
                        mundo.cambiarVisual(visualInicioY + 1, visualInicioX, True)
                        mundo.cambiarVisual((visualInicioY + 1), (visualInicioX + 1), True)
                        mundo.cambiarVisual((visualInicioY + 1), (visualInicioX - 1), True)
                        print("Eje Y Descubridor: " + str(visualInicioY))
                        print("Eje X Descubridor: " + str(visualInicioX))
                    else:
                        visualInicioY -= 1
                        mundo.ponerPelado(visualInicioY, visualInicioX)

                if event.key == pygame.K_UP:
                    inicioCeldaY += escalaY
                    if inicioCeldaY > 0:
                        inicioCeldaY = 0
                    
                    print("Eje Y Lista: "+str(inicioCeldaY))
                    print("Eje X Lista: "+str(inicioCeldaX))

                if event.key == pygame.K_w:
                    mundo.sacarPelado(visualInicioY, visualInicioX)
                    visualInicioY -=1
                    if visualInicioY < 1:
                        visualInicioY = 1
                    if (type(mundo.getTerreno(visualInicioY, visualInicioX)) == Tierra 
                    and type(mundo.getNaturaleza(visualInicioY, visualInicioX)) == Aire):

                        mundo.ponerPelado(visualInicioY, visualInicioX)
                        print(type(mundo.getTerreno(visualInicioY,visualInicioX)))

                        mundo.cambiarVisual(visualInicioY, visualInicioX, True)
                        mundo.cambiarVisual(visualInicioY, (visualInicioX + 1), True)
                        mundo.cambiarVisual(visualInicioY, (visualInicioX - 1), True)
                        mundo.cambiarVisual((visualInicioY - 1), visualInicioX, True)
                        mundo.cambiarVisual((visualInicioY - 1), (visualInicioX + 1), True)
                        mundo.cambiarVisual((visualInicioY - 1), (visualInicioX - 1), True)
                        print("Eje Y Descubridor: " + str(visualInicioY))
                        print("Eje X Descubridor: " + str(visualInicioX))
                    else:
                        visualInicioY += 1
                        mundo.ponerPelado(visualInicioY, visualInicioX)

                if event.key == pygame.K_RIGHT:
                    inicioCeldaX -= escalaX
                    if inicioCeldaX < -7560:
                        inicioCeldaX = -7560
                    
                    print("Eje Y Lista: "+str(inicioCeldaY))
                    print("Eje X Lista: "+str(inicioCeldaX))

                if event.key == pygame.K_d:
                    mundo.sacarPelado(visualInicioY, visualInicioX)
                    visualInicioX +=1
                    if visualInicioX > 213:
                        visualInicioX = 213
                    if (type(mundo.getTerreno(visualInicioY, visualInicioX)) == Tierra 
                    and type(mundo.getNaturaleza(visualInicioY, visualInicioX)) == Aire):

                        mundo.ponerPelado(visualInicioY, visualInicioX)
                        print(type(mundo.getTerreno(visualInicioY,visualInicioX)))

                        mundo.cambiarVisual(visualInicioY, visualInicioX, True)
                        mundo.cambiarVisual((visualInicioY - 1), visualInicioX, True)
                        mundo.cambiarVisual((visualInicioY + 1), visualInicioX, True)
                        mundo.cambiarVisual(visualInicioY, (visualInicioX + 1), True)
                        mundo.cambiarVisual((visualInicioY - 1), visualInicioX + 1, True)
                        mundo.cambiarVisual((visualInicioY + 1), visualInicioX + 1, True)
                        print("Eje Y Descubridor: " + str(visualInicioY))
                        print("Eje X Descubridor: " + str(visualInicioX))
                    else:
                        visualInicioX -= 1
                        mundo.ponerPelado(visualInicioY, visualInicioX)

                if event.key == pygame.K_LEFT:
                    inicioCeldaX += escalaX
                    if inicioCeldaX > 0:
                        inicioCeldaX = 0

                    print("Eje Y Lista: "+str(inicioCeldaY))
                    print("Eje X Lista: "+str(inicioCeldaX))

                if event.key == pygame.K_a:
                    mundo.sacarPelado(visualInicioY, visualInicioX)
                    visualInicioX -=1
                    if visualInicioX < 1:
                        visualInicioX = 1
                    if (type(mundo.getTerreno(visualInicioY, visualInicioX)) == Tierra and type(mundo.getNaturaleza(visualInicioY, visualInicioX)) == Aire):
                    
                        mundo.ponerPelado(visualInicioY, visualInicioX)
                        print(type(mundo.getTerreno(visualInicioY,visualInicioX)))

                        mundo.cambiarVisual(visualInicioY, visualInicioX, True)
                        mundo.cambiarVisual((visualInicioY - 1), visualInicioX, True)
                        mundo.cambiarVisual((visualInicioY + 1), visualInicioX, True)
                        mundo.cambiarVisual(visualInicioY, (visualInicioX - 1), True)
                        mundo.cambiarVisual((visualInicioY - 1), visualInicioX - 1, True)
                        mundo.cambiarVisual((visualInicioY + 1), visualInicioX - 1, True)
                        print("Eje Y Descubridor: " + str(visualInicioY))
                        print("Eje X Descubridor: " + str(visualInicioX))
                    else: 
                        visualInicioX += 1
                        mundo.ponerPelado(visualInicioY, visualInicioX)

    if menu.getActivo() == True:
        pantalla.blit(menu.getFondo(),(0,0))
        pantalla.blit(menu.getStartSup(), menu.getStartRect())
        pantalla.blit(menu.getExitSup(), menu.getExitRect())

    else:    

        pos_y=inicioCeldaY
        pantalla.blit(fondo_copado, (0, 0))
        
        for i in range(0, celdasY):
            for x in range(0, celdasX):
                if mundo.getVisual(i,x) == True:
<<<<<<< HEAD
                    if mundo.getPelado(i,x) == True:

                        if type(mundo.getTerreno(i,x)) == Tierra:
                            pantalla.blit(pasto_fond, (pos_x, pos_y))
                            
                            if type(mundo.getNaturaleza(i, x)) == Arbol:
                                pantalla.blit(arbol_sup, (pos_x, pos_y))

                            elif type(mundo.getNaturaleza(i, x)) == Montana:
                                pantalla.blit(montaña_sup, (pos_x, pos_y))
                            
                        else:
                            pantalla.blit(agua_fond, (pos_x, pos_y))
=======
                    if type(mundo.getTerreno(i,x)) == Tierra:
                        pantalla.blit(pasto_fond, (pos_x, pos_y))
>>>>>>> 1957675adf06ff9027a245c52f24127357a59c13
                        
                        if type(mundo.getNaturaleza(i, x)) == Arbol:
                            pantalla.blit(arbol_sup, (pos_x, pos_y))
                        elif type(mundo.getNaturaleza(i, x)) == Montana:
                            pantalla.blit(montaña_sup, (pos_x, pos_y))

                    else:
                        pantalla.blit(agua_fond, (pos_x, pos_y))
                    if mundo.getPelado(i,x) == "Pelado":
                        pantalla.blit(pelado_sup, (pos_x, pos_y))
                else:
                    pantalla.blit(negro_fond, (pos_x, pos_y))
                pos_x+=escalaX
            pos_x=inicioCeldaX
            pos_y+=escalaY

    pygame.display.update()
    fps.tick(60)