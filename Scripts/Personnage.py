import pygame

class Personnage():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        self.coordx = 50
        self.coordy = 50
        self.vie = 200
        self.armure = 0
        self.vitesse = 256
    
    def charger_sprite(self, chemin_sprite):
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))

    def move(self, arg, delta):
        '''Permet d'executer les instructions nécéssaires au déplacement du personnage'''
        if arg == "right":
            self.coordx += self.vitesse * delta
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base droite.png")

        if arg == "left":
            self.coordx -= self.vitesse * delta
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        
        if arg == "jump":
            self.coordy -= 20
        #Multiplier 20 par la viscosité du liquide dans lequel est le joueur.

    def gravité(self):
        '''Applique la gravité au personnage en fonction des liquides'''
        self.coordy += 0

    def afficher(self, screen):
        '''Permet d'afficher le personnage sur l'écran'''
        screen.blit(self.sprite, (self.coordx, self.coordy))                 