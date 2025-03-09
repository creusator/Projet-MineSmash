import pygame
from Variables_Globales import *
from Blocs import Grille

vecteur = pygame.math.Vector2

class Personnage():
    def __init__(self,key_left, key_right, key_jump, key_run, chemin_sprite):
        self.sprite = self.charger_sprite(chemin_sprite)
        self.sprite_facing_right = self.sprite
        self.sprite_facing_left = pygame.transform.flip(self.sprite, True, False)
        self.keybinds = {'move_left': key_left, 'move_right': key_right, 'jump': key_jump, 'run': key_run}
        self.vie = 20
        self.armure = 20
        self.coord = vecteur(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.velocity = vecteur(0, 0)
        self.acceleration = vecteur(0, 0)
        self.walk_acceleration_value = 15
        self.run_acceleration_value = 20
        self.friction_value = -8
        self.gravity_value = 9.81
        self.max_fall_speed = 3
        self.max_walk_speed = 1.5
        self.max_run_speed = 12
        self.jump_force = 5
        self.is_jumping = False
        self.is_on_ground = False
        self.collision_box = pygame.Rect(0, 0,TILE_SIZE, TILE_SIZE * 2)
        
    def charger_sprite(self, chemin_sprite:str) -> pygame.surface.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (TILE_SIZE, TILE_SIZE * 2))

    def player_collision_list(self, collision_list:list) -> list:
        '''Renvoie la liste des blocs avec lequel le joueur a des collisions'''
        hit_list = []
        for bloc in collision_list:
            if self.collision_box.colliderect(bloc):
                hit_list.append(bloc)
        return hit_list

    def check_collision_x(self, grille_collision_list:list) -> None:
        '''Corrige les déplacements horizontaux du personnage'''
        collision_list = self.player_collision_list(grille_collision_list)
        for bloc in collision_list :
            if self.velocity.x > 0:
                self.coord.x = bloc.left - self.collision_box.w
                self.collision_box.x = self.coord.x
            if self.velocity.x < 0:
                self.coord.x = bloc.right
                self.collision_box.x = self.coord.x

    def check_collision_y(self, grille_collision_list:list) -> None:
        '''Corrige les déplacements verticaux du personnage'''
        self.is_on_ground = False
        self.collision_box.bottom += 1
        collison_list = self.player_collision_list(grille_collision_list)
        for bloc in collison_list :
            if self.velocity.y > 0:
                self.is_on_ground = True
                self.is_jumping = False
                self.velocity.y = 0
                self.coord.y = bloc.top
                self.collision_box.bottom = self.coord.y
            if self.velocity.y < 0 :
                self.velocity.y = 0
                self.coord.y = bloc.bottom + self.collision_box.h
                self.collision_box.bottom = self.coord.y

    def limit_horizontal_velocity(self, limit:int) -> None:
        '''Limite la vélocité horizontale en fonction de limit'''
        limit *= TILE_SIZE

        if self.velocity.x > limit:
            self.velocity.x = limit
        elif self.velocity.x < -limit:
            self.velocity.x = -limit

        if -0.1 < self.velocity.x < 0.1:
            self.velocity.x = 0
    
    def limit_vertical_velocity(self, limit:int) -> None:
        '''Limite la vélocité verticale en fonction de limite'''
        limit *= TILE_SIZE

        if self.velocity.y > limit:
            self.velocity.y = limit
        elif self.velocity.y < -limit:
            self.velocity.y = -limit

    def horizontal_movement(self, delta_time:float) -> None:
        '''Applique les déplacements horizontaux en fonction des touches'''
        self.acceleration.x = 0
        key = pygame.key.get_pressed()

        if key[self.keybinds['move_left']]:
            self.sprite = self.sprite_facing_left
            if key[self.keybinds['run']] :
                self.acceleration.x -= self.run_acceleration_value * TILE_SIZE
            else :
                self.acceleration.x -= self.walk_acceleration_value * TILE_SIZE

        elif key[self.keybinds['move_right']]:
            self.sprite = self.sprite_facing_right
            if key[self.keybinds['run']] :
                self.acceleration.x += self.run_acceleration_value * TILE_SIZE
            else :
                self.acceleration.x += self.walk_acceleration_value * TILE_SIZE

        self.acceleration.x += self.velocity.x * self.friction_value
        self.velocity.x += self.acceleration.x * delta_time  

        if key[self.keybinds['run']]:
            self.limit_horizontal_velocity(self.max_run_speed)
        else :  
            self.limit_horizontal_velocity(self.max_walk_speed)

        self.coord.x += self.velocity.x * delta_time
        self.collision_box.x = self.coord.x

    def vertical_movement(self, delta_time:float) -> None:
        '''Applique la gravité, limite la vélocité verticale du joueur'''
        self.velocity.y += self.gravity_value * delta_time
        self.limit_vertical_velocity(self.max_fall_speed)
        self.coord.y += self.velocity.y * delta_time * TILE_SIZE
        self.collision_box.bottom = self.coord.y
    
    def jump(self) -> None:
        '''Permet de sauter si le personnage est sur le sol'''
        if self.is_on_ground:
            self.is_jumping = True
            self.velocity.y -= self.jump_force
            self.is_on_ground = False

    def move(self,grille:Grille, delta:float) -> None:
        '''Applique les fonctions ci dessus pour les déplacements'''
        grille_collision_list = grille.get_collison_list()
        self.horizontal_movement(delta)
        self.check_collision_x(grille_collision_list)
        self.vertical_movement(delta)
        self.check_collision_y(grille_collision_list)

    def debug(self, screen:pygame.surface.Surface) -> None:
        """Affiche à l'écran des graphisme de debug, visualisation des collisions ect..."""
        pygame.draw.rect(screen, BLUE, self.collision_box)

    def afficher(self, screen:pygame.surface.Surface) -> None:
        '''Permet d'afficher le personnage sur l'écran'''
        #self.debug(screen)
        screen.blit(self.sprite, (self.collision_box.x, self.collision_box.y))