import pygame, sys

pygame.init()
pantalla = pygame.display.set_mode((800,500))

pygame.display.set_caption('Lo barato sale caro lo normal es lo raro')
fps = pygame.time.Clock()

font_copado = pygame.font.Font(None, 50)

fondo_copado = pygame.Surface((800,500))
fondo_copado.fill((190, 190, 190))
piton_copada = pygame.image.load('Fotuchas/python_copada.png').convert_alpha()
piton_copada = pygame.transform.scale(piton_copada, (50, 50))

frase_copada = font_copado.render('Mira mama estoy en la tele', False, (205, 173, 0))

piton_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
            
    pantalla.blit(fondo_copado, (0,0))
    pantalla.blit(frase_copada, (180,50))

    piton_x_pos -= 4
    if piton_x_pos < -400: piton_x_pos = 800
    pantalla.blit(piton_copada, (piton_x_pos, 100))

    pygame.display.update()
    fps.tick(60)
    
