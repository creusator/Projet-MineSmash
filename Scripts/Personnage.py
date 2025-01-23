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
        self.velocity = vecteur(0, 0)
        self.acceleration = vecteur(0, 0)
        self.acceleration_value = 1
        self.friction_value = -0.35
        self.gravite = 9.81
        self.terminal_velocity = 7
        self.jump_force = 8
        self.jumping = False
        self.is_on_ground = False
        self.collision_box = pygame.Rect(0, 0,64,128)

    def charger_sprite(self, chemin_sprite:str) -> pygame.surface.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))
    
    def player_collision_list(self, collision_list:list) -> list:
        '''Renvoie la liste des blocs avec lequel le joueur a des collisions'''
        hit_list = []
        for bloc in collision_list:
            if self.collision_box.colliderect(bloc):
                hit_list.append(bloc)
        return hit_list

    def check_collision_x(self, grille):
        collision_list = self.player_collision_list(grille.get_collison_list())
        for bloc in collision_list :
            if self.velocity.x > 0:
                self.coord.x = bloc.left - self.collision_box.w
                self.collision_box.x = self.coord.x
            if self.velocity.x < 0:
                self.coord.x = bloc.right
                self.collision_box.x = self.coord.x

    def check_collision_y(self, grille):
        self.is_on_ground = False
        self.collision_box.bottom += 1
        collison_list = self.player_collision_list(grille.get_collison_list())
        for bloc in collison_list :
            if self.velocity.y > 0:
                self.is_on_ground = True
                self.jumping = False
                self.velocity.y = 0
                self.coord.y = bloc.top
                self.collision_box.bottom = self.coord.y
            if self.velocity.y < 0 :
                self.velocity.y = 0
                self.coord.y = bloc.bottom + self.collision_box.h
                self.collision_box.bottom = self.coord.y

    def horizontal_movement(self, delta_time):
        self.acceleration.x = 0
        key = pygame.key.get_pressed()

        if key[pygame.K_q]:
            self.acceleration.x -= self.acceleration_value
        elif key[pygame.K_d]:
            self.acceleration.x += self.acceleration_value
        
        self.acceleration.x += self.velocity.x * self.friction_value
        self.velocity.x += self.acceleration.x * delta_time       
        self.velocity_limit(128)
        self.coord.x += self.velocity.x * delta_time - (self.acceleration.x * 0.5) * (delta_time * delta_time)
        self.collision_box.x = self.coord.x

    def vertical_movement(self, delta_time):
        self.velocity.y += self.gravite * delta_time

        if self.velocity.y > self.terminal_velocity : 
            self.velocity.y = self.terminal_velocity 
        
        self.coord.y += self.gravite * delta_time - (self.acceleration.y * 0.5) * (delta_time * delta_time)
        self.collision_box.bottom = self.coord.y

    def velocity_limit(self, limit):
        self.velocity.x = max(-limit, min(self.velocity.x, limit))
        if abs(self.velocity.x) < .01: self.velocity.x = 0
    
    def jump(self):
        if self.is_on_ground:
            self.jumping = True
            self.velocity.y -= self.jump_force
            self.is_on_ground = False

    def move(self,grille, delta):
        self.horizontal_movement(delta)
        self.check_collision_x(grille)
        self.vertical_movement(delta)
        self.check_collision_y(grille)

    def debug(self, screen:pygame.surface.Surface) -> None:
        """Affiche à l'écran des graphisme de debug, visualisation des collisions ect..."""
        pygame.draw.rect(screen, BLUE, self.collision_box)
        screen.blit(self.pos_indicator, (self.coord.x, self.coord.y - 140)) #Tete du joueur

    def afficher(self, screen:pygame.surface.Surface) -> None:
        '''Permet d'afficher le personnage sur l'écran'''
        self.debug(screen)
        screen.blit(self.sprite, (self.collision_box.x, self.collision_box.y))