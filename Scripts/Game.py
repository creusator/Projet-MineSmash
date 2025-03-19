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
grille.chunk = grille.charger(CHEMIN_CHUNK)
inventaire = Inventaire()
barre_outil = Barre_outil()
barre_vie = Barre_vie()
barre_armure = Barre_armure()
Game = Game()

while running:

    delta = clock.get_time()/1000
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            grille.sauvegarder()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                inventaire.ouvrir()
            if event.key == player1.keybinds['jump']:
                player1.jump()
            if event.key == player2.keybinds['jump']:
                player2.jump()

        if event.type == pygame.MOUSEBUTTONDOWN:  
            x, y = grille.get_coord_grille((mouse_x, mouse_y))
            if event.button == 1:
                grille.detruire_bloc(x, y)
            elif event.button == 3:
                grille.placer_bloc(x, y, barre[barre_outil.slot])
        if event.type == pygame.MOUSEWHEEL:
            if event.y == -1: 
                barre_outil.scroll("up")
            elif event.y == 1:
                barre_outil.scroll("down")

    screen.fill(SKY_BLUE)
    grille.dessiner(screen)
    player1.afficher(screen)
    player2.afficher(screen)
    player1.move(grille, delta)
    player2.move(grille, delta)
    barre_outil.afficher(screen)
    barre_armure.afficher(screen,player1.armure)
    barre_vie.afficher(screen, player1.vie)
    inventaire.afficher(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()