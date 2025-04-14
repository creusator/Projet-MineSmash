import pygame
import json
from Variables_Globales import *

class Grille():
    def __init__(self):
        self.largeur_grille = SCREEN_WIDTH
        self.hauteur_grille = SCREEN_HEIGHT
        self.taille_case = TILE_SIZE
        self.chunk = None

    def charger(self, chemin_chunk:str) -> list:
        """Renvoi une matrice utilisable a partir du chemin d'accès du JSON"""
        chunk = open(chemin_chunk, 'r')
        return json.load(chunk)

    def sauvegarder(self) -> None:
        with open(CHEMIN_CHUNK, 'w') as chemin_sauvegarde:
            json.dump(self.chunk, chemin_sauvegarde)

    def placer_bloc(self, x:int, y:int, bloc:int) -> None:
        """Place le bloc 'bloc' la grille au coordonées du curseur. """
        if 0 <= y < len(self.chunk) and 0 <= x < len(self.chunk[0]):
            if self.chunk[y][x] == 0 :
                self.chunk[y][x] = bloc

    def detruire_bloc(self, x:int, y:int) -> None:
        if 0 <= y < len(self.chunk) and 0 <= x < len(self.chunk[0]):
            self.chunk[y][x] = 0

    def get_coord_grille(self, pos:tuple) -> tuple:
        """Prend des coordonées et renvoie les coordonées de la grille associé"""
        x, y = pos
        return int(x // self.taille_case), int(y // self.taille_case)

    def get_bloc(self, pos:tuple) -> int:
        """Prend des coordonées et renvoie le bloc de la grille associé"""
        x, y = pos
        return self.chunk[int(y // self.taille_case)][int(x // self.taille_case)]

    def get_collison_list(self) -> list:
        """Place et renvoie une liste de rect qui représente les blocs solides de la grille"""
        collision_list = []
        for y, ligne in enumerate(self.chunk):
            for x, bloc_id in enumerate(ligne):
                bloc = identify_bloc(bloc_id)
                coordbloc = (x * self.taille_case, y * self.taille_case)
                if type(bloc) is Solide :
                    bloc.collision_box.topleft = coordbloc
                    collision_list.append(bloc.collision_box)
        return collision_list

    def dessiner(self, screen:pygame.surface.Surface) -> None:
        """Dessine les blocs sur l'écran en fontion des données de la matrice"""
        for y, ligne in enumerate(self.chunk):
            for x, bloc_id in enumerate(ligne):
                bloc = identify_bloc(bloc_id)
                coordbloc = (x * self.taille_case, y * self.taille_case)
                screen.blit(bloc.sprite, coordbloc)

class Bloc() :
    def __init__(self, chemin_sprite:str):
        self.sprite = self.charger_sprite(chemin_sprite)
        self.collision_box = pygame.Rect(0,0,TILE_SIZE,TILE_SIZE)

    def charger_sprite(self, chemin_sprite:str) -> pygame.Surface:
        """Renvoi un sprite utilisable redimensionné en fonction de la taille des blocs"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (TILE_SIZE, TILE_SIZE)).convert_alpha()

class Solide(Bloc) :
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)
        self.durete : 0
        self.is_flammable = False
        self.has_collision = True

class Liquide(Bloc) : 
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)
        self.damages = 0
        self.viscosity = 0.0

def identify_bloc(bloc_id:int):
    '''Retourne un bloc ainsi que tout ces attributs et son rect en fonction d'un id'''
    if bloc_id == 0 :
        return air()
    if bloc_id == 1 :
        return stone_block()
    if bloc_id == 2 :
        return grass_block()
    if bloc_id == 3 :
        return dirt_block()

def stone_block() -> Solide:
    '''Crée un bloc de pierre'''
    stone_block = Solide('Asset/image/Blocs/bloc_stone.png')
    stone_block.durete = 10
    return stone_block

def grass_block() -> Solide:
    '''Crée un bloc d'herbe'''
    grass_block = Solide('Asset/image/Blocs/bloc_herbe.png')
    grass_block.durete = 5
    return grass_block

def dirt_block() -> Solide:
    '''Crée un bloc de terre'''
    dirt_block = Solide('Asset/image/Blocs/bloc_terre.png')
    dirt_block.durete = 5
    return dirt_block

def air() -> Liquide:
    '''Crée un bloc d'air'''
    air = Liquide('Asset/image/Blocs/air.png')
    air.viscosite = 0.0
    return air

def eau() -> Liquide:
    '''Crée un bloc d'eau'''
    eau = Liquide('Asset/image/Blocs/bloc_stone.png')
    eau.viscosite = 0.6
    return eau 

def lave() -> Liquide:
    '''Crée un bloc de lave'''
    lave = Liquide('Asset/image/Blocs/bloc_stone.png')
    lave.vicosite = 0.6
    leve.degats = 5 
    return lave 
