import pygame
from Blocs import Grille

vecteur = pygame.math.Vector2
BLUE = (0, 0, 255)

class Personnage():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        self.pos_indicator = pygame.image.load("Asset/image/personnage/pos_indicator.png")
        self.vie = 20
        self.armure = 20
        self.coord = vecteur(480, 512/2)
        self.velocite = vecteur(0, 0)
        self.acceleration = vecteur(0, 0)
        self.gravite = 0.81
        self.jump_force = 13
        self.jumping = False
        self.collision_box = pygame.Rect(0, 0,64,128)

    def charger_sprite(self, chemin_sprite:str) -> pygame.surface.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))
    
    def jump(self, grille):
        collision_tete = grille.get_bloc((self.coord.x, self.coord.y - 140))
        if self.is_on_ground(grille) and collision_tete == 0:
            self.jumping = True
    
    def update_pos(self, grille:list, delta:float) -> None :
        '''Permet d'exécuter les instructions nécessaires au déplacements du personnage'''
        key = pygame.key.get_pressed()
        self.acceleration = vecteur(0,self.gravite)
        self.collision_box.topleft = (self.coord.x - 32, self.coord.y - 128)

        ACCELERATION = 0.5
        FRICTION = -0.12

        if self.is_on_ground(grille):
            if self.jumping :
                self.jumping = False
                self.velocite.y -= self.jump_force
            else :
                self.velocite.y = 0
                self.acceleration.y = 0

        if key[pygame.K_q]:
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
            if self.colliding_left(grille) == False:
                self.acceleration.x = -ACCELERATION
            else :
                self.acceleration.x = 0
                self.velocite.x = 0
                
        if key[pygame.K_d]: 
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base droite.png")
            if self.colliding_right(grille) == False:
                self.acceleration.x = ACCELERATION
            else :
                self.acceleration.x = 0
                self.velocite.x = 0

        self.acceleration.x += self.velocite.x * FRICTION
        self.velocite += self.acceleration
        self.coord += self.velocite + self.acceleration * delta

    def is_on_ground(self, grille:list) -> bool:
        '''Renvoi un booleen qui permet de savoir si le personnage touche le sol ou non'''
        collision_pied_gauche = grille.get_bloc((self.coord.x - 16, self.coord.y))
        collision_pied_droit = grille.get_bloc((self.coord.x + 16, self.coord.y))
        return collision_pied_droit != 0 or collision_pied_gauche != 0

    def colliding_left(self, grille:list) -> bool:
        '''Renvoi un booleen si le personnage touche un bloc a gauche'''
        collision_bas_gauche = grille.get_bloc((self.coord.x - 24, self.coord.y - 16))
        collision_milieu_gauche = grille.get_bloc((self.coord.x - 24, self.coord.y - 64))
        collision_haut_gauche = grille.get_bloc((self.coord.x - 24, self.coord.y - 115))
        return collision_bas_gauche != 0 or collision_milieu_gauche != 0 or collision_haut_gauche != 0
    
    def colliding_right(self, grille:list) -> bool:
        '''Renvoi un booleen si le personnage touche un bloc a droite'''
        collision_bas_droite = grille.get_bloc((self.coord.x + 24, self.coord.y - 16))
        collision_milieu_droite = grille.get_bloc((self.coord.x + 24, self.coord.y - 64))
        collision_haut_droite = grille.get_bloc((self.coord.x +   24, self.coord.y - 115))
        return collision_bas_droite != 0 or collision_milieu_droite != 0 or collision_haut_droite != 0

    def debug(self, screen:pygame.surface.Surface) -> None:
        """Affiche à l'écran des graphisme de debug, visualisation des collisions ect..."""
        pygame.draw.rect(screen, BLUE, self.collision_box)
        screen.blit(self.pos_indicator, (self.coord.x, self.coord.y - 140)) #Tête du joueur
        screen.blit(self.pos_indicator, (self.coord.x - 16, self.coord.y)) #Pieds gauche du joueur
        screen.blit(self.pos_indicator, (self.coord.x + 16, self.coord.y)) #Pieds droit du joueur
        screen.blit(self.pos_indicator, (self.coord.x - 24, self.coord.y - 16)) #Bas gauche
        screen.blit(self.pos_indicator, (self.coord.x + 24, self.coord.y - 16)) #Bas droit
        screen.blit(self.pos_indicator, (self.coord.x - 24, self.coord.y - 64)) #Milieu gauche
        screen.blit(self.pos_indicator, (self.coord.x + 24, self.coord.y - 64)) #Milieu droit
        screen.blit(self.pos_indicator, (self.coord.x - 24, self.coord.y - 115)) #Haut gauche
        screen.blit(self.pos_indicator, (self.coord.x + 24, self.coord.y - 115)) #Haut droit

    def afficher(self, screen:pygame.surface.Surface) -> None:
        '''Permet d'afficher le personnage sur l'écran'''
        self.debug(screen)
        screen.blit(self.sprite, (self.coord.x - 32, self.coord.y - 128))
        