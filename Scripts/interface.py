import pygame

class Inventaire():
    def __init__(self):
        self.inventaire = self.charger_inventaire("Asset/image/interface/inventaire.png")
        self.vide = self.charger_inventaire("Asset/image/Blocs/air.png")
        self.coordx = 512
        self.coordy = 256

    def charger_inventaire(self, chemin_inventaire):
        """Renvoi un inventaire utilisable redimensionné en 128*98"""
        return pygame.transform.scale(pygame.image.load(chemin_inventaire), (256, 196))

    def ouvrir(self):
        if self.constante==0:
            pass
        elif self.constante==1:
            pass
        else :
            return 0

    def afficher(self, screen):
        constante=0
        if constante==0:
            screen.blit(self.inventaire, (self.coordx, self.coordy))
            constante+=1
        elif constante==1:
            screen.blit(self.vide, (self.coordx, self.coordy))
            constante-=1
        else:
            return 0