import pygame
from Blocs import *
from Personnage import *

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
FRAMERATE = 30

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

p1 = Personnage()

while running:

    delta = clock.tick(FRAMERATE)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Personnage.move(p1, "left")
            if event.key == pygame.K_RIGHT:
                Personnage.move(p1, "right")
            if event.key == pygame.K_SPACE:
                Personnage.move(p1, "jump")
            if event.key == pygame.K_e:
                pass

    screen.fill((135,206,235))
    position_bloc(screen, liste_bloc)
    screen.blit(p1.sprite, (p1.coordx, p1.coordy))
    p1.afficher(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()
