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

player = Personnage()
grille = Grille(SCREEN_WIDTH, SCREEN_HEIGHT, 64)
grille.chunk = grille.charger("Save/monde-test/chunk1.json")
inventaire = Inventaire()
barre_outil = Barre_outil()
barre_vie = Barre_vie()
barre_armure = Barre_armure()

while running:

    delta = clock.tick(FRAMERATE)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                inventaire.ouvrir()
            if event.key == pygame.K_SPACE:
                player.jump(grille)
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            x, y = grille.get_coord_grille(event.pos)
            if event.button == 1:
                grille.detruire_bloc(x, y)
            elif event.button == 3:
                grille.placer_bloc(x, y, 1)
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                barre_outil.scroll("up")
            elif event.y == -1:
                barre_outil.scroll("down")

    screen.fill((135,206,235))
    player.afficher(screen)
    player.update_pos(grille, delta)
    grille.dessiner(screen)
    barre_outil.afficher(screen)
    barre_armure.afficher(screen,player.armure)
    barre_vie.afficher(screen, player.vie)
    inventaire.afficher(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()