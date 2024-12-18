import pygame, sys
from pygame.locals import *
h_i=480 #hauteur interface
l_i=980 #largeur interface
pygame.init()
interface=pygame.display.set_mode((l_i,h_i))
interface.fill((255,255,255))

x=0
y=0
l=70 # Largeur
h=70 # Hauteur
for y in range(0, interface.get_height(), h ):
    for x in range(0, interface.get_width(), l ):
        pygame.draw.rect(interface, (0,0,0), (x, y, l, h), 1)

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()