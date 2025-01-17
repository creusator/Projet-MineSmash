import pygame

class Inventaire():
    def __init__(self):
        self.inventaire = self.charger_inventaire("Asset/image/interface/inventaire.png")
        self.vide = self.charger_inventaire("Asset/image/Blocs/air.png")
        self.coordx = 256
        self.coordy = 64
        self.constante = 0

    def charger_inventaire(self, chemin_inventaire:str) -> pygame.surface.Surface:
        """Renvoi un inventaire utilisable redimensionné en 128*98"""
        return pygame.transform.scale(pygame.image.load(chemin_inventaire), (512, 392))

    def ouvrir(self) -> None:
        if self.constante == 0:
            self.constante = 1
        elif self.constante == 1:
            self.constante = 0

    def afficher(self, scree:pygame.surface.Surface) -> None:
        if self.constante == 0:
            screen.blit(self.vide, (self.coordx, self.coordy))
        if self.constante == 1:
            screen.blit(self.inventaire, (self.coordx, self.coordy))

class Barre_outil():

    def __init__ (self):
        self.constante = 1
        self.coordx = 256
        self.coordy = 400
        self.barre = self.charger_barre("Asset/image/interface/barre d'inventaire.png")
        self.largeur,self.hauteur = self.barre.get_size()
        self.valeur = 0
    
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en 4680 * 96"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (4680, 96))

    def afficher(self, screen:pygame.surface.Surface) -> None:
        if self.constante <= 0:
            self.constante = 9
        elif self.constante >= 10:
            self.constante = 1
        screen.blit(self.barre,(self.coordx,self.coordy),[(520*(self.constante-1)),0,520,self.hauteur])

    def scroll(self,arg:str) -> None:
        if arg == "up":
            self.constante+=1
        elif arg == "down":
            self.constante-=1


class Barre_vie():

    def __init__ (self):
        self.constante = 1
        self.coordx = 255
        self.coordy = 365
        self.barre = self.charger_barre("Asset/image/interface/barre de vie.png")
        self.largeur,self.hauteur = self.barre.get_size()
        self.valeur = 0
        
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en 5166 * 24"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (5166, 24))

    def afficher(self, screen:pygame.surface.Surface, vie:int) -> None:
        screen.blit(self.barre,(self.coordx,self.coordy),[246*(20-vie),0,246,self.hauteur])

class Barre_armure():

    def __init__ (self):
        self.constante = 1
        self.coordx = 535
        self.coordy = 365
        self.barre = self.charger_barre("Asset/image/interface/barre d'armure.png")
        self.largeur,self.hauteur = self.barre.get_size()
        self.valeur = 0
    
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en 5166 * 24"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (5166, 24))
    
    def afficher(self, screen:pygame.surface.Surface, armure:int) -> None:
        screen.blit(self.barre,(self.coordx,self.coordy),[246*(20-armure),0,246,self.hauteur])