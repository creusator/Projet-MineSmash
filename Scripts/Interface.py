import pygame

class Inventaire():
    def __init__(self):
        self.inventaire = self.charger_inventaire("Asset/image/interface/inventaire.png")
        self.vide = self.charger_inventaire("Asset/image/Blocs/air.png")
        self.coordx = 256
        self.coordy = 64
        self.is_open = False

    def charger_inventaire(self, chemin_inventaire:str) -> pygame.surface.Surface:
        """Renvoi un inventaire utilisable redimensionné en 512*392"""
        return pygame.transform.scale(pygame.image.load(chemin_inventaire), (512, 392))

    def ouvrir(self) -> None:
        """Permet de récupérer l'interaction pour ouvrir ou fermer l'inventaire"""
        if self.is_open == False:
            self.is_open = True
        elif self.is_open == True:
            self.is_open = False

    def afficher(self, screen:pygame.surface.Surface) -> None:
        """Récupère le bool de self.is_open pour afficher ou désafficher l'inventaire"""
        if self.is_open == 0:
            screen.blit(self.vide, (self.coordx, self.coordy))
        if self.is_open == 1:
            screen.blit(self.inventaire, (self.coordx, self.coordy))

class Barre_outil():

    def __init__ (self):
        self.slot = 1
        self.coordx = 256
        self.coordy = 400
        self.barre = self.charger_barre("Asset/image/interface/barre d'inventaire.png")
        self.largeur,self.hauteur = self.barre.get_size()
    
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en 4680 * 96"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (4680, 96))

    def afficher(self, screen:pygame.surface.Surface) -> None:
        """Affiche la barre d'inventaire et permete de changer de slot dans Game.py"""
        if self.slot <= 0:
            self.slot = 9
        elif self.slot >= 10:
            self.slot = 1
        screen.blit(self.barre,(self.coordx,self.coordy),[(520*(self.slot-1)),0,520,self.hauteur])

    def scroll(self,arg:str) -> None:
        """Récupére la valeur de scroll dans Game.py"""
        if arg == "up":
            self.slot+=1
        elif arg == "down":
            self.slot-=1


class Barre_vie():

    def __init__ (self):
        self.coordx = 255
        self.coordy = 365
        self.barre = self.charger_barre("Asset/image/interface/barre de vie.png")
        self.largeur,self.hauteur = self.barre.get_size()
        
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en 5166 * 24"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (5166, 24))

    def afficher(self, screen:pygame.surface.Surface, vie:int) -> None:
        """Affiche la barre de vie et est relié a la vie de Personnage.py"""
        screen.blit(self.barre,(self.coordx,self.coordy),[246*(20-vie),0,246,self.hauteur])

class Barre_armure():

    def __init__ (self):
        self.coordx = 535
        self.coordy = 365
        self.barre = self.charger_barre("Asset/image/interface/barre d'armure.png")
        self.largeur,self.hauteur = self.barre.get_size()
    
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en 5166 * 24"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (5166, 24))
    
    def afficher(self, screen:pygame.surface.Surface, armure:int) -> None:
        """Affiche la barre d'armure et est relié a l'armure de Personnage.py"""
        screen.blit(self.barre,(self.coordx,self.coordy),[246*(20-armure),0,246,self.hauteur])