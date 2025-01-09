import pygame

class Inventaire():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/interface/inventaire.png")
        self.vide = self.charger_sprite("Asset/image/Blocs/air.png")
    

    def charger_sprite(self, chemin_sprite):
        """Renvoi un sprite utilisable redimensionné en 128*98"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (128, 98))

    def ouvrir(self, screen):
        constante=0
        if constante==0:
            screen.blit(self.sprite, (512, 256))
            constante+=1
        if constante==1:
            screen.blit(self.vide, (512, 256))
            constante-=1
        else :
            return 0