import pygame
from Blocs import *
from Personnage import *
from Interface import *

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
FRAMERATE = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True

p1 = Personnage()
grille = Grille(SCREEN_WIDTH, SCREEN_HEIGHT, 64)
grille.chunk = grille.charger("Save/monde-test/chunk1.json")
inventaire=Inventaire()

while running:

    delta = clock.tick(FRAMERATE)/1000
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.move("jump", delta)
            if event.key == pygame.K_e:
                inventaire.ouvrir(screen)

    if key[pygame.K_q]:
        p1.move("left", delta)
    if key[pygame.K_d]:
        p1.move("right", delta)
        

    screen.fill((135,206,235))
    grille.dessiner(screen)
    p1.gravité()
    p1.afficher(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()
