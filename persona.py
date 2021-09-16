class Persona:
    '''Una persona que en realidad es un pelado'''
    
    def __init__(self, persona):
        self.persona = persona


    def cambiarPelado(self, persona):
        '''Cambia el atributo persona'''
        self.persona = persona
    

    def ponerPelado(self):
        self.cambiarPelado(True)

    def sacarPelado(self):
        self.cambiarPelado(False)
        
    def getPersona(self):
        return self.persona