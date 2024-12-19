import pygame

pygame.init()
screen = pygame.display.set_mode((64, 64))
clock = pygame.time.Clock()

class Bloc() :
    def __init__(self, sprite):
        self.sprite = None
        self.id = None
    
    def placer(self):
        """Place le bloc au coordonées du curseur. """

    def detruire(self):
        """Notes pour plus tard :
            Si le bloc est solide --> détruire
            Si le bloc est liquide et que le joueur à un seau --> mettre dans le seau"""
    
    def draw(self):
        return self.sprite
    
class Solide(Bloc) :
    def __init__(self, sprite):
        super().__init__(sprite)
        self.durete : 0
        self.is_flammable = False

class Liquide(Bloc) : 
    def __init__(self):
        super().__init__()
        self.degats : 0
        self.viscosite : 0

class Personnage():
    def __init__(self):
        self.coordx = 0
        self.coordy = 0
        self.vie = 200
        self.armure = 0
        self.vitesse = 10

cobble = Solide(pygame.transform.scale(pygame.image.load('Asset/image/Blocs/bloc_stone.png'), (64, 64)))
print(str(cobble.sprite))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(cobble.draw(), (0, 0))

    pygame.display.flip()
    clock.tick(4)
    screen.fill("White")

pygame.quit()
