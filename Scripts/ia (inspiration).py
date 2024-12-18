# Créé par Elève, le 18/12/2024 en Python 3.7
import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
tile_size = 50
cols, rows = 16, 12
width, height = cols * tile_size, rows * tile_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minecraft 2D")

# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

# Variables du jeu
player_pos = [width // 2, height // 2]
inventory = {"grass": 0, "dirt": 0, "water": 0}
world = [["grass" if row > 8 else "dirt" if row > 6 else "water" for col in range(cols)] for row in range(rows)]
selected_block = "grass"

# Charger des images
textures = {
    "grass": pygame.Surface((tile_size, tile_size)),
    "dirt": pygame.Surface((tile_size, tile_size)),
    "water": pygame.Surface((tile_size, tile_size)),
}
textures["grass"].fill(GREEN)
textures["dirt"].fill(BROWN)
textures["water"].fill(BLUE)

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player_pos[0] -= tile_size
            if event.key == K_RIGHT:
                player_pos[0] += tile_size
            if event.key == K_UP:
                player_pos[1] -= tile_size
            if event.key == K_DOWN:
                player_pos[1] += tile_size
            if event.key == K_1:
                selected_block = "grass"
            if event.key == K_2:
                selected_block = "dirt"
            if event.key == K_3:
                selected_block = "water"
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = x // tile_size, y // tile_size

            if event.button == 1:  # Clic gauche: Collecter un bloc
                block = world[grid_y][grid_x]
                inventory[block] += 1
                world[grid_y][grid_x] = ""
            elif event.button == 3:  # Clic droit: Placer un bloc
                if inventory[selected_block] > 0:
                    world[grid_y][grid_x] = selected_block
                    inventory[selected_block] -= 1

    # Dessiner le monde
    for row in range(rows):
        for col in range(cols):
            block = world[row][col]
            if block:
                screen.blit(textures[block], (col * tile_size, row * tile_size))

    # Dessiner le joueur
    pygame.draw.rect(screen, (255, 0, 0), (*player_pos, tile_size, tile_size))

    # Afficher l'inventaire
    inventory_text = f"Inventory: Grass={inventory['grass']} Dirt={inventory['dirt']} Water={inventory['water']}"
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(inventory_text, True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

    # Mettre à jour l'écran
    pygame.display.flip()
    clock.tick(30)

pygame.quit()

