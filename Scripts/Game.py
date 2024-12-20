import pygame

class Bloc() :
    def __init__(self, chemin_sprite):
        self.sprite = self.charger_sprite(chemin_sprite)
        self.id = None

    def charger_sprite(self, chemin_sprite):
        """Renvoi un sprite utilisable redimensionné en 64x64"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 64))

    def placer(self):
        """Place le bloc SUR la GRILLE au coordonées du curseur. """

    def detruire(self):
        """Notes pour plus tard :
            Si le bloc est solide --> mettre dans l'inventaire / détruire
            Si le bloc est liquide et que le joueur à un seau --> mettre dans le seau"""
    
class Solide(Bloc) :
    def __init__(self, id, chemin_sprite):
        super().__init__(chemin_sprite)
        self.durete : 0
        self.is_flammable = False


class Liquide(Bloc) : 
    def __init__(self, sprite):
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

def stone_block():
    stone_block = Solide(1, 'Asset/image/Blocs/bloc_stone.png')
    return stone_block

def grass_block():
    stone_block = Solide(1, 'Asset/image/Blocs/bloc_herbe.png')
    return stone_block

def dirt_block():
    stone_block = Solide(1, 'Asset/image/Blocs/bloc_terre.png')
    return stone_block

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
cobble = Solide(1, 'Asset/image/Blocs/bloc_stone.png')


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(stone_block().sprite, (0, 0))
    screen.blit(grass_block().sprite, (64, 0))
    screen.blit(dirt_block().sprite, (64, 64))

    pygame.display.flip()
    clock.tick(4)
    screen.fill("White")

pygame.quit()
