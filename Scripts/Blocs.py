import pygame
from Game import *

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
        self.has_collision = True

class Liquide(Bloc) : 
    def __init__(self, sprite):
        super().__init__()
        self.degats : 0
        self.viscosite : 0

def position_bloc(li):
    x=0
    y=256
    for a in li:
        x=0
        for b in a:
            if b==[]:
                x+=64
            else:
                screen.blit(b.sprite,(x, y))
                x+=64
        y+=64

def stone_block():
    stone_block = Solide(1, 'Asset/image/Blocs/bloc_stone.png')
    stone_block.durete = 10
    return stone_block

def grass_block():
    grass_block = Solide(2, 'Asset/image/Blocs/bloc_herbe.png')
    grass_block.durete = 5
    return grass_block

def dirt_block():
    dirt_block = Solide(3, 'Asset/image/Blocs/bloc_terre.png')
    dirt_block.durete = 5
    return dirt_block

