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
inventaire=Inventaire()

while running:

    delta = clock.tick(FRAMERATE)/1000
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p1.jump(grille.get_bloc(grille.get_coord_grille((p1.coordx, p1.coordy))), grille.get_bloc(grille.get_coord_grille((p1.coordx, p1.coordy - 140))))
            if event.key == pygame.K_e:
                inventaire.ouvrir()
        if event.type == pygame.MOUSEBUTTONDOWN:  
            x, y = grille.get_coord_grille(event.pos)
            if event.button == 1:
                grille.detruire_bloc(x, y)
            elif event.button == 3:
                grille.placer_bloc(x, y, 1)

    if key[pygame.K_q]:
        p1.move("left",grille.get_bloc(grille.get_coord_grille((p1.coordx - 32, p1.coordy - 64))),grille.get_bloc(grille.get_coord_grille((p1.coordx - 32, p1.coordy - 128))), delta)
    if key[pygame.K_d]:  
        p1.move("right",grille.get_bloc(grille.get_coord_grille((p1.coordx + 32, p1.coordy - 64))),grille.get_bloc(grille.get_coord_grille((p1.coordx +   32, p1.coordy - 128))), delta)

    screen.fill((135,206,235))
    p1.afficher(screen)
    p1.gravité(grille.get_bloc(grille.get_coord_grille((p1.coordx, p1.coordy))))
    grille.dessiner(screen)
    inventaire.afficher(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()