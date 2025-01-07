import pygame

class Personnage():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/personnage/skin de base.png")
        self.coordx = 50
        self.coordy = 50
        self.vie = 200
        self.armure = 0
        self.vitesse = 10
    
    def charger_sprite(self, chemin_sprite):
        """Renvoi un sprite utilisable redimensionné en 64x64"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))

    def move(self, arg):
        if arg == "right":
            self.coordx += self.vitesse

        if arg == "left":
            self.coordx -= self.vitesse
        
        if arg == "jump":
            coordy += 10
        #Multiplier 10 par la viscosité du liquide dans lequel est le joueur.

    def afficher(self, screen):
        screen.blit(self.sprite, (self.coordx, self.coordy))