import pygame
from Blocs import *
class Personnage():
    def __init__(self):
        self.coordx = 0
        self.coordy = 0
        self.vie = 200
        self.armure = 0
        self.vitesse = 10

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True

liste_bloc=[
    [grass_block(),grass_block(),grass_block(),grass_block(),grass_block(),grass_block(),grass_block(),grass_block(),grass_block(),grass_block()],
    [dirt_block(),dirt_block(),dirt_block(),dirt_block(),dirt_block(),dirt_block(),dirt_block(),dirt_block(),dirt_block(),dirt_block()],
    [stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block()],
    [stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block(),stone_block()]
]

def position_bloc(li):
    x=0
    y=0
    for a in li:
        x=0
        for b in a:
            if b==[]:
                x+=64
            else:
                screen.blit(b.sprite,(x, y))
                x+=64
        y+=64

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135,206,235))
    position_bloc(liste_bloc)
    pygame.display.flip()
    clock.tick(4)
pygame.quit()
