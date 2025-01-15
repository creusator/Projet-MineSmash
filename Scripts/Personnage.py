import pygame
from Blocs import Grille

class Personnage():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        self.pos_indicator = pygame.image.load("Asset/image/personnage/pos_indicator.png")
        self.coordx, self.coordy = 448, 256
        self.vie = 200
        self.armure = 0
        self.acceleration_x = 400
        self.acceleration_y = 50
        self.velocite_x = 100
        self.velocite_x_max = 256
        self.velocite_y = 0
        self.velocite_y_max = 50
        self.force_saut = 1000
        self.gravite = 0.50

    def charger_sprite(self, chemin_sprite:str) -> pygame.surface.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))

    def move(self, direction:str , grille:list, delta:float) -> None:
        '''Permet d'exécuter les instructions nécessaires au déplacements du personnage'''
        if direction == "right":
            bloc_grille_bas = grille.get_bloc(grille.get_coord_grille((self.coordx + 24, self.coordy - 16)))
            bloc_grille_milieu = grille.get_bloc(grille.get_coord_grille((self.coordx + 24, self.coordy - 64)))
            bloc_grille_haut = grille.get_bloc(grille.get_coord_grille((self.coordx +   24, self.coordy - 128)))

            if bloc_grille_bas == 0 and bloc_grille_milieu == 0 and bloc_grille_haut == 0 :
                self.sprite = self.charger_sprite("Asset/image/personnage/skin de base droite.png")
                if self.velocite_x < self.velocite_x_max :
                    self.velocite_x += self.acceleration_x * delta
                else :
                    self.velocite_x = 256
                self.coordx += self.velocite_x * delta

        if direction == "left":
            bloc_grille_bas = grille.get_bloc(grille.get_coord_grille((self.coordx - 24, self.coordy - 16)))
            bloc_grille_milieu = grille.get_bloc(grille.get_coord_grille((self.coordx - 24, self.coordy - 64)))
            bloc_grille_haut = grille.get_bloc(grille.get_coord_grille((self.coordx - 24, self.coordy - 128)))

            if bloc_grille_bas == 0 and bloc_grille_milieu == 0 and bloc_grille_haut == 0 :
                self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
                if self.velocite_x < self.velocite_x_max:
                    self.velocite_x += self.acceleration_x * delta
                else :
                    self.velocite_x = 256
                self.coordx -= self.velocite_x * delta

    def jump(self, grille:list, delta:float) -> None:
        bloc_grille_pied_gauche = grille.get_bloc(grille.get_coord_grille((self.coordx - 16, self.coordy)))
        bloc_grille_pied_droit = grille.get_bloc(grille.get_coord_grille((self.coordx + 16, self.coordy)))
        bloc_grille_tete = grille.get_bloc(grille.get_coord_grille((self.coordx, self.coordy - 140)))

        if bloc_grille_pied_gauche != 0 or bloc_grille_pied_droit != 0 and bloc_grille_tete == 0:
            if self.velocite_y < self.velocite_y_max :
                self.velocite_y += self.force_saut * delta
            else :
                self.velocite_y = 0
            self.coordy -= self.velocite_y

    def gravité(self, grille:list, delta:float) -> None:
        '''Applique la gravité au personnage en fonction des bloc en dessous'''
        bloc_grille_pied_gauche = grille.get_bloc(grille.get_coord_grille((self.coordx - 16, self.coordy)))
        bloc_grille_pied_droit = grille.get_bloc(grille.get_coord_grille((self.coordx + 16, self.coordy)))
        if bloc_grille_pied_gauche == 0 and bloc_grille_pied_droit == 0 :
            if self.velocite_y < self.velocite_y_max :
                self.velocite_y += self.velocite_y + self.gravite * delta
                self.coordy += self.velocite_y
            else:
                self.velocite_y = 0
        else :
            self.velocite_y = 0

    def debug(self, screen:pygame.surface.Surface) -> None:
        """Affiche à l'écran des graphisme de debug, visualisation des collisions ect..."""
        screen.blit(self.pos_indicator, (self.coordx, self.coordy - 140)) #Tête du joueur
        screen.blit(self.pos_indicator, (self.coordx - 16, self.coordy)) #Pieds gauche du joueur
        screen.blit(self.pos_indicator, (self.coordx + 16, self.coordy)) #Pieds droit du joueur
        screen.blit(self.pos_indicator, (self.coordx - 24, self.coordy - 16)) #Bas gauche
        screen.blit(self.pos_indicator, (self.coordx + 24, self.coordy - 16)) #Bas droit
        screen.blit(self.pos_indicator, (self.coordx - 24, self.coordy - 64)) #Milieu gauche
        screen.blit(self.pos_indicator, (self.coordx + 24, self.coordy - 64)) #Milieu droit
        screen.blit(self.pos_indicator, (self.coordx - 24, self.coordy - 128)) #Haut gauche
        screen.blit(self.pos_indicator, (self.coordx + 24, self.coordy - 128)) #Haut droit

    def afficher(self, screen:pygame.surface.Surface) -> None:
        '''Permet d'afficher le personnage sur l'écran'''
        screen.blit(self.sprite, (self.coordx - 32, self.coordy - 128))
        self.debug(screen)