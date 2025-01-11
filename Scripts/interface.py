import pygame

class Inventaire():
    def __init__(self):
        self.inventaire = self.charger_inventaire("Asset/image/interface/inventaire.png")
        self.vide = self.charger_inventaire("Asset/image/Blocs/air.png")
        self.coordx = 256
        self.coordy = 64
        self.constante = 0

    def charger_inventaire(self, chemin_inventaire):
        """Renvoi un inventaire utilisable redimensionné en 128*98"""
        return pygame.transform.scale(pygame.image.load(chemin_inventaire), (512, 392))

    def ouvrir(self):
        if self.constante == 0:
            self.constante = 1
        elif self.constante == 1:
            self.constante = 0

    def afficher(self, screen):
        if self.constante == 0:
            screen.blit(self.vide, (self.coordx, self.coordy))
        if self.constante == 1:
            screen.blit(self.inventaire, (self.coordx, self.coordy))
        