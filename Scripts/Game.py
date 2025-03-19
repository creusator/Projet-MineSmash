import pygame
from Variables_Globales import *
from Blocs import *
from Personnage import *
from Interface import *
from cycle_jour_nuit import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
 
player1 = Personnage(pygame.K_q, pygame.K_d, pygame.K_z, pygame.K_LSHIFT,"Asset/image/personnage/skin de base.png")
player2 = Personnage(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_0, "Asset/image/personnage/skin alternatif.png")
grille = Grille()
grille.chunk = grille.charger("Save/monde-test/chunk1.json")
inventaire = Inventaire()
barre_outil = Barre_outil()
barre_vie = Barre_vie()
barre_armure = Barre_armure()
Ui = Ui()
Game = Game()

while running:

    delta = clock.get_time()/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                inventaire.ouvrir()
            if event.key == player1.keybinds['jump']:
                player1.jump()
            if event.key == player2.keybinds['jump']:
                player2.jump()

        if event.type == pygame.MOUSEBUTTONDOWN:  
            x, y = grille.get_coord_grille(event.pos)
            if event.button == 1:
                grille.detruire_bloc(x, y)
            elif event.button == 3:
                grille.placer_bloc(x, y, 1)
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1: 
                barre_outil.scroll("up")
            elif event.y == -1:
                barre_outil.scroll("down")

    screen.fill(SKY_BLUE)
    grille.dessiner(screen)
    player1.afficher(screen)
    player2.afficher(screen)
    player1.move(grille, delta)
    player2.move(grille, delta)
    Ui.afficher(player1, screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()