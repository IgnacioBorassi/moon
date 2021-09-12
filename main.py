class main:
    '''Ejecuta el juego'''
    def __init__(self):
        self.visual = Visual()


    def inicio(self):
        self.visual.cargar()

if __name__ == '__main__':
    import pygame 
    pygame.init()
    from diversion import Visual
    

    main = main()
    main.inicio()
