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
 
player = Personnage()
grille = Grille()
grille.chunk = grille.charger("Save/monde-test/chunk1.json")
inventaire = Inventaire()
barre_outil = Barre_outil()
barre_vie = Barre_vie()
barre_armure = Barre_armure()
Game = Game()

while running:

    delta = clock.get_time()/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                inventaire.ouvrir()
            if event.key == pygame.K_SPACE:
                player.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if player.is_jumping:
                    player.velocity.y *= 0.25
                    player.is_jumping = False

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

    if clock.get_fps() < 31:
        screen.fill((255,0,0))
    else :
        screen.fill((0,255, 0))
    grille.dessiner(screen)
    player.afficher(screen)
    player.move(grille, delta)
    barre_outil.afficher(screen)
    barre_armure.afficher(screen,player.armure)
    barre_vie.afficher(screen, player.vie)
    inventaire.afficher(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)
pygame.quit()