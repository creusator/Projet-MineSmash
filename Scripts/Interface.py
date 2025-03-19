import pygame
import json
from Variables_Globales import *

class Ui():
    def __init__(self):
        self.id_interface = 0
        self.show_barre = True
        self.show_inventaire = False
        self.vide = self.charger_vide("Asset/image/Blocs/air.png")
        
    def affchage(self):
        ''' vie, armure, barre d'inventaire'''
        if self.id_interface == 0:
            return self.show_barre == True
        elif self.id_interface != 0:
            return self.show_barre == False
        '''inventaire'''
        if self.id_interface == 1:
            return self.show_inventaire == True
        elif self.id_interface != 1:
            return self.show_inventaire == False
    
    def charger_vide(self, chemin_vide:str) -> pygame.surface.Surface:
        """Renvoi un sprite vide utilisable redimensionné en fontion de la taille de l'écran"""
        return pygame.transform.scale(pygame.image.load(chemin_vide), (1, 1))
    

    def afficher(self, player ,screen:pygame.surface.Surface) -> None:
        barre_outil.afficher(screen)
        barre_armure.afficher(screen,player.armure)
        barre_vie.afficher(screen, player.vie)
        inventaire.afficher(screen)

class Inventaire(Ui):
    def __init__(self):
        super().__init__()
        self.inventaire = self.charger_inventaire("Asset/image/interface/inventaire.png")
        self.coordx = SCREEN_WIDTH * 0.25
        self.coordy = SCREEN_HEIGHT * 0.12
        self.is_open = False

    def charger_inventaire(self, chemin_inventaire:str) -> pygame.surface.Surface:
        """Renvoi un sprite d'inventaire utilisable redimensionné en fontion de la taille de l'écran"""
        return pygame.transform.scale(pygame.image.load(chemin_inventaire), (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.7))

    def ouvrir(self) -> None:
        """Permet de récupérer l'interaction pour ouvrir ou fermer l'inventaire"""
        if self.id_interface != 1:
            self.is_open = True
            self.id_interface = 1
        elif self.id_interface == 1:
            self.is_open = False 
            self.id_interface = 0

    def afficher(self, screen:pygame.surface.Surface) -> None:
        """Récupère le bool de self.is_open pour afficher ou désafficher l'inventaire"""
        if self.is_open == True:
            screen.blit(self.inventaire, (self.coordx, self.coordy))
        elif self.is_open == False:
            screen.blit(self.vide, (self.coordx, self.coordy))

class Barre_outil(Ui):

    def __init__ (self):
        super().__init__()
        self.slot = 1
        self.coordx = SCREEN_WIDTH * 0.25
        self.coordy = SCREEN_HEIGHT * 0.8
        self.barre = self.charger_barre("Asset/image/interface/barre d'inventaire.png")
        self.largeur,self.hauteur = self.barre.get_size()
    
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en fonction de la taille de l'écran"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (SCREEN_WIDTH * 4.57, SCREEN_HEIGHT * 0.18))

    def afficher(self, screen:pygame.surface.Surface) -> None:
        """Affiche la barre d'inventaire et permete de changer de slot dans Game.py"""
        if self.slot <= 0:
            self.slot = 9
        elif self.slot >= 10:
            self.slot = 1
        if self.show_barre == True:
            screen.blit(self.barre,(self.coordx,self.coordy),[((self.largeur/9) * (self.slot-1)), 0, (self.largeur/9), self.hauteur])
        elif self.show_barre == False:
            screen.blit(self.vide, (self.coordx, self.coordy))

    def scroll(self,arg:str) -> None:
        """Récupére la valeur de scroll dans Game.py"""
        if arg == "up":
            self.slot+=1
        elif arg == "down":
            self.slot-=1


class Barre_vie(Ui):

    def __init__ (self):
        super().__init__()
        #self.coordx = 255
        #self.coordy = 365
        self.coordx = SCREEN_WIDTH*0.25
        self.coordy = SCREEN_HEIGHT*0.73
        self.barre = self.charger_barre("Asset/image/interface/barre de vie.png")
        self.largeur,self.hauteur = self.barre.get_size()
        
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en fonction de la taille de l'écran"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (SCREEN_WIDTH * 5.01, SCREEN_HEIGHT * 0.05))

    def afficher(self, screen:pygame.surface.Surface, vie:int) -> None:
        """Affiche la barre de vie et est relié a la vie de Personnage.py"""
        screen.blit(self.barre,(self.coordx,self.coordy),[(self.largeur/21)*(20-vie),0,(self.largeur/21),self.hauteur])

class Barre_armure(Ui):

    def __init__ (self):
        super().__init__()
        #self.coordx = 535
        #self.coordy = 365
        self.coordx = SCREEN_WIDTH*0.52
        self.coordy = SCREEN_HEIGHT*0.73
        self.barre = self.charger_barre("Asset/image/interface/barre d'armure.png")
        self.largeur,self.hauteur = self.barre.get_size()
    
    def charger_barre(self, chemin_barre:str) -> pygame.surface.Surface:
        """Renvoi une barre utilisable redimensionné en 5166 * 24"""
        return pygame.transform.scale(pygame.image.load(chemin_barre), (SCREEN_WIDTH * 5.1, SCREEN_HEIGHT * 0.05))
    
    def afficher(self, screen:pygame.surface.Surface, armure:int) -> None:
        """Affiche la barre d'armure et est relié a l'armure de Personnage.py"""
        screen.blit(self.barre,(self.coordx,self.coordy),[(self.largeur/21)*(20-armure),0,(self.largeur/21),self.hauteur])