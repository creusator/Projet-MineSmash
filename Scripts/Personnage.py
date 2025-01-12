import pygame

class Personnage():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        self.coordx = 512
        self.coordy = 256
        self.vie = 200
        self.armure = 0
        self.vitesse = 256
    
    def charger_sprite(self, chemin_sprite):
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))

    def move(self, direction, delta):
        '''Permet d'executer les instructions nécéssaires au déplacement du personnage'''
        if direction == "right":
            self.coordx += self.vitesse * delta
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base droite.png")

        if direction == "left":
            self.coordx -= self.vitesse * delta
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")

    def jump(self, coord_grille:tuple):
        self.coordy -= 128

    def gravité(self,bloc_grille):
        '''Applique la gravité au personnage en fonction des bloc en dessous'''
        if bloc_grille == 0  :
            self.coordy += 7 

    def afficher(self, screen):
        '''Permet d'afficher le personnage sur l'écran'''
        screen.blit(self.sprite, (self.coordx - 32, self.coordy - 128))
        screen.blit(pygame.image.load("Asset\image\personnage\pos_indicator.png"), (self.coordx, self.coordy))