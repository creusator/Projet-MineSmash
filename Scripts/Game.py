import pygame
from Blocs import *
from Personnage import *
from Interface import *

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512
TILE_SIZE = 64
FRAMERATE = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
 
player = Personnage()
grille = Grille(SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE)
grille.chunk = grille.charger("Save/monde-test/chunk1.json")
inventaire = Inventaire()
barre_outil = Barre_outil()
barre_vie = Barre_vie()
barre_armure = Barre_armure()

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

    screen.fill((135,206,235))
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