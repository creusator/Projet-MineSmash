import pygame
from Blocs import *
from Personnage import *
from interface import *

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
inventaire = Inventaire()
barre_outil = Barre_outil()

while running:

    delta = clock.tick(FRAMERATE)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                inventaire.ouvrir()
            if event.key == pygame.K_SPACE:
                p1.jump(grille)
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            x, y = grille.get_coord_grille(event.pos)
            if event.button == 1:
                grille.detruire_bloc(x, y)
            elif event.button == 3:
                grille.placer_bloc(x, y, 1)
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                barre_outil.scroll("haut")
            elif event.y == -1:
                barre_outil.scroll("bas")

    screen.fill((135,206,235))
    p1.afficher(screen)
    p1.move(grille, delta)
    grille.dessiner(screen)
    barre_outil.afficher(screen)
    inventaire.afficher(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()