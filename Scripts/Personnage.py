import pygame
from Blocs import Grille

vecteur = pygame.math.Vector2

class Personnage():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        self.pos_indicator = pygame.image.load("Asset/image/personnage/pos_indicator.png")
        self.vie = 200
        self.armure = 0
        self.coord = vecteur(480, 512/2)
        self.velocite = vecteur(0, 0)
        self.acceleration = vecteur(0, 0)
        self.gravite = 0.81
        self.jump_force = 13
        self.jumping = False

    def charger_sprite(self, chemin_sprite:str) -> pygame.surface.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))
    
    def jump(self, grille):
        collision_tete = grille.get_bloc((self.coord.x, self.coord.y - 140))
        if self.is_on_ground(grille) and collision_tete == 0:
            self.jumping = True
    
    def update(self, grille:list, delta:float) -> None :
        '''Permet d'exécuter les instructions nécessaires au déplacements du personnage'''
        collision_bas_droite = grille.get_bloc((self.coord.x + 24, self.coord.y - 16))
        collision_milieu_droite = grille.get_bloc((self.coord.x + 24, self.coord.y - 64))
        collision_haut_droite = grille.get_bloc((self.coord.x +   24, self.coord.y - 128))
        collision_bas_gauche = grille.get_bloc((self.coord.x - 24, self.coord.y - 16))
        collision_milieu_gauche = grille.get_bloc((self.coord.x - 24, self.coord.y - 64))
        collision_haut_gauche = grille.get_bloc((self.coord.x - 24, self.coord.y - 128))
        collision_tete = grille.get_bloc((self.coord.x, self.coord.y - 140))

        key = pygame.key.get_pressed()
        self.acceleration = vecteur(0,self.gravite)

        ACCELERATION = 0.5
        FRICTION = -0.12

        if key[pygame.K_q]:
            self.acceleration.x = -ACCELERATION
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        if key[pygame.K_d]:
            self.acceleration.x = ACCELERATION
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base droite.png")

        if self.is_on_ground(grille):
            if self.jumping :
                self.jumping = False
                self.velocite.y -= self.jump_force
            else :
                self.velocite.y = 0
                self.acceleration.y = 0

        self.acceleration.x += self.velocite.x * FRICTION
        self.velocite += self.acceleration
        self.coord += self.velocite + self.acceleration * delta

    def is_on_ground(self, grille):
        collision_pied_gauche = grille.get_bloc((self.coord.x - 16, self.coord.y))
        collision_pied_droit = grille.get_bloc((self.coord.x + 16, self.coord.y))
        return collision_pied_droit != 0 or collision_pied_gauche != 0

    def debug(self, screen:pygame.surface.Surface) -> None:
        """Affiche à l'écran des graphisme de debug, visualisation des collisions ect..."""
        screen.blit(self.pos_indicator, (self.coord.x, self.coord.y - 140)) #Tête du joueur
        screen.blit(self.pos_indicator, (self.coord.x - 16, self.coord.y)) #Pieds gauche du joueur
        screen.blit(self.pos_indicator, (self.coord.x + 16, self.coord.y)) #Pieds droit du joueur
        screen.blit(self.pos_indicator, (self.coord.x - 24, self.coord.y - 16)) #Bas gauche
        screen.blit(self.pos_indicator, (self.coord.x + 24, self.coord.y - 16)) #Bas droit
        screen.blit(self.pos_indicator, (self.coord.x - 24, self.coord.y - 64)) #Milieu gauche
        screen.blit(self.pos_indicator, (self.coord.x + 24, self.coord.y - 64)) #Milieu droit
        screen.blit(self.pos_indicator, (self.coord.x - 24, self.coord.y - 128)) #Haut gauche
        screen.blit(self.pos_indicator, (self.coord.x + 24, self.coord.y - 128)) #Haut droit

    def afficher(self, screen:pygame.surface.Surface) -> None:
        '''Permet d'afficher le personnage sur l'écran'''
        screen.blit(self.sprite, (self.coord.x - 32, self.coord.y - 128))
        self.debug(screen)