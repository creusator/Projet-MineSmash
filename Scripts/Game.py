import pygame
from Blocs import *
from Personnage import *

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

while running:

    delta = clock.tick(30)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_q:
            Personnage.move("left", delta)
        if event.type == pygame.K_d:
            Personnage.move("right", delta)
        if event.type == pygame.K_SPACE:
            Personnage.move("jump", delta)
        if event.type == pygame.K_e:
            pass

    screen.fill((135,206,235))
    position_bloc(screen, liste_bloc)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
