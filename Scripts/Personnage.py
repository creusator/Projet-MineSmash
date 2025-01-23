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
        self.collision_types = {'top' : False, 'bottom' : False, 'right' : False, 'left' : False}
        self.moving_left = False
        self.moving_right = False

    def charger_sprite(self, chemin_sprite:str) -> pygame.surface.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))
    
    def jump(self, grille):
        collision_tete = grille.get_bloc((self.coord.x, self.coord.y - 140))
        if self.is_on_ground(grille) and collision_tete == 0:
            self.jumping = True
    
    def player_collision_list(self, rect:pygame.Rect, collision_list:list) -> list:
        '''Renvoie la liste des blocs avec lequel le joueur a des collisions'''
        hit_list = []
        for bloc in collision_list:
            if rect.colliderect(bloc):
                hit_list.append(bloc)
        return hit_list

    def update_collision_x(self, grille:list) -> None :
        '''Met a jour la liste des collisions en fonction des mouvements latéraux'''
        self.collision_box.topleft = (self.coord.x - 32, self.coord.y - 128)
        collision_list = self.player_collision_list(self.collision_box, grille.get_collison_list())

        self.collision_types['right'] = False
        self.collision_types['left'] = False

        for bloc in collision_list:
            if self.velocite.x > 0:
                self.collision_types['right'] = True
                self.velocite.x = 0
                self.acceleration.x = 0
            elif self.velocite.x < 0:
                self.collision_types['left'] = True
                self.velocite.x = 0
                self.acceleration.x = 0

        self.coord.x = self.collision_box.centerx
    
    def update_collision_y(self, grille):
        '''Met a jour la liste des collisions en fonction des mouvements verticaux'''
        self.collision_box.topleft = (self.coord.x - 32, self.coord.y - 128)
        collision_list = self.player_collision_list(self.collision_box, grille.get_collison_list())

        self.collision_types['top'] = False
        self.collision_types['bottom'] = False

        for bloc in collision_list:
            if self.velocite.y > 0:
                self.collision_types['bottom'] = True
                self.collision_box.bottom = bloc.top
                self.velocite.y = 0
                self.acceleration.y = 0
            elif self.velocite.y < 0:
                self.collision_types['top'] = True
                self.collision_box.top = bloc.bottom
                self.velocite.y = 0
                self.acceleration.y = 0

        self.coord.y = self.collision_box.bottom

    def move(self,grille, delta):
        ACCELERATION = 0.5
        FRICTION = -0.12

        self.acceleration = vecteur(0,self.gravite)

        self.update_collision_x(grille)
        if self.moving_left:
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
            self.acceleration.x = -ACCELERATION
        if self.moving_right :
            self.sprite = self.charger_sprite("Asset/image/personnage/skin de base droite.png")
            self.acceleration.x = ACCELERATION
        
        self.update_collision_y(grille)
        if self.collision_types['bottom']:
            if self.jumping :
                self.jumping = False
                self.velocite.y -= self.jump_force
            else :
                self.velocite.y = 0
                self.acceleration.y = 0

        self.acceleration.x += self.velocite.x * FRICTION
        self.velocite += self.acceleration
        self.coord += self.velocite + self.acceleration * delta
        self.collision_box.topleft = (self.coord.x - 32, self.coord.y - 128)

    def debug(self, screen:pygame.surface.Surface) -> None:
        """Affiche à l'écran des graphisme de debug, visualisation des collisions ect..."""
        pygame.draw.rect(screen, BLUE, self.collision_box)
        screen.blit(self.pos_indicator, (self.coord.x, self.coord.y - 140)) #Tete du joueur

    def afficher(self, screen:pygame.surface.Surface) -> None:
        '''Permet d'afficher le personnage sur l'écran'''
        self.debug(screen)
        screen.blit(self.sprite, (self.collision_box.x, self.collision_box.y))
        