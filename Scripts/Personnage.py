import pygame

class Personnage():
    def __init__(self):
        self.sprite = pygame.image.load("Asset/image/personnage/skin de base.png")
        self.coordx = 50
        self.coordy = 50
        self.vie = 200
        self.armure = 0
        self.vitesse = 10

    def move(self, arg, delta):
        if arg == "right":
            self.coordx += self.vitesse * delta

        if arg == "left":
            self.coordx -= self.vitesse * delta
        
        if arg == "jump":
            coordy += 10
        #Multiplier 10 par la viscosité du liquide dans lequel est le joueur.