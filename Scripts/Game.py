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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(stone_block().sprite, (0, 448))
    screen.blit(stone_block().sprite, (0, 384))
    screen.blit(grass_block().sprite, (0, 256))
    screen.blit(dirt_block().sprite, (0, 320))
    screen.blit(stone_block().sprite, (64, 448))
    screen.blit(stone_block().sprite, (64, 384))
    screen.blit(grass_block().sprite, (64, 256))
    screen.blit(dirt_block().sprite, (64, 320))
    screen.blit(stone_block().sprite, (128, 448))
    screen.blit(stone_block().sprite, (128, 384))
    screen.blit(grass_block().sprite, (128, 256))
    screen.blit(dirt_block().sprite, (128, 320))
    screen.blit(stone_block().sprite, (192, 448))
    screen.blit(stone_block().sprite, (192, 384))
    screen.blit(grass_block().sprite, (192, 256))
    screen.blit(dirt_block().sprite, (192, 320))
    screen.blit(stone_block().sprite, (256, 448))
    screen.blit(stone_block().sprite, (256, 384))
    screen.blit(grass_block().sprite, (256, 256))
    screen.blit(dirt_block().sprite, (256, 320))
    screen.blit(stone_block().sprite, (320, 448))
    screen.blit(stone_block().sprite, (320, 384))
    screen.blit(grass_block().sprite, (320, 256))
    screen.blit(dirt_block().sprite, (320, 320))
    screen.blit(stone_block().sprite, (384, 448))
    screen.blit(stone_block().sprite, (384, 384))
    screen.blit(grass_block().sprite, (384, 256))
    screen.blit(dirt_block().sprite, (384, 320))
    screen.blit(stone_block().sprite, (448, 448))
    screen.blit(stone_block().sprite, (448, 384))
    screen.blit(grass_block().sprite, (448, 256))
    screen.blit(dirt_block().sprite, (448, 320))
    screen.blit(stone_block().sprite, (512, 448))
    screen.blit(stone_block().sprite, (512, 384))
    screen.blit(grass_block().sprite, (512, 256))
    screen.blit(dirt_block().sprite, (512, 320))
    screen.blit(stone_block().sprite, (576, 448))
    screen.blit(stone_block().sprite, (576, 384))
    screen.blit(grass_block().sprite, (576, 256))
    screen.blit(dirt_block().sprite, (576, 320))

    pygame.display.flip()
    clock.tick(4)
    screen.fill((135,206,235))

pygame.quit()
