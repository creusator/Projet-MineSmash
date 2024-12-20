import pygame
from Blocs import *
class Personnage():
    def __init__(self):
        self.coordx = 0
        self.coordy = 0
        self.vie = 200
        self.armure = 0
        self.vitesse = 10

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True

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
