import pygame
import json

class Grille():
    def __init__(self, largeur_grille:int, hauteur_grille:int, taille_case:int):
        self.largeur_grille = largeur_grille
        self.hauteur_grille = hauteur_grille
        self.taille_case = taille_case
        self.chunk = None

    def charger(self, chemin_chunk:str) -> list:
        """Renvoi une matrice utilisable a partir du chemin d'accès du JSON"""
        chunk = open(chemin_chunk, 'r')
        return json.load(chunk)

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

    def dessiner(self, screen:pygame.surface.Surface) -> None:
        """Dessine les blocs sur l'écran en fontion des données de la matrice"""
        for y, ligne in enumerate(self.chunk):
            for x, bloc in enumerate(ligne):
                if bloc == 0 :
                    screen.blit(air().sprite, (x * self.taille_case, y * self.taille_case))
                if bloc == 1 :
                    screen.blit(stone_block().sprite, (x * self.taille_case, y * self.taille_case))
                if bloc == 2 :
                    screen.blit(grass_block().sprite, (x * self.taille_case, y * self.taille_case))
                if bloc == 3 :
                    screen.blit(dirt_block().sprite, (x * self.taille_case, y * self.taille_case))

class Bloc() :
    def __init__(self, chemin_sprite:str):
        self.sprite = self.charger_sprite(chemin_sprite)
        self.collision_box = pygame.rect
        self.id = None

    def charger_sprite(self, chemin_sprite:str) -> pygame.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x64"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 64))

class Solide(Bloc) :
    def __init__(self, id:int, chemin_sprite:str):
        super().__init__(chemin_sprite)
        self.durete : 0
        self.is_flammable = False
        self.has_collision = True

class Liquide(Bloc) : 
    def __init__(self, id:int, chemin_sprite:str):
        super().__init__(chemin_sprite)
        self.degats : 0
        self.viscosite : 0.0

def stone_block() -> Solide:
    '''Crée un bloc de pierre'''
    stone_block = Solide(1, 'Asset/image/Blocs/bloc_stone.png')
    stone_block.durete = 10
    return stone_block

def grass_block() -> Solide:
    '''Crée un bloc d'herbe'''
    grass_block = Solide(2, 'Asset/image/Blocs/bloc_herbe.png')
    grass_block.durete = 5
    return grass_block

def dirt_block() -> Solide:
    '''Crée un bloc de terre'''
    dirt_block = Solide(3, 'Asset/image/Blocs/bloc_terre.png')
    dirt_block.durete = 5
    return dirt_block

def air() -> Liquide:
    '''Crée un bloc d'air'''
    air = Liquide(0, 'Asset/image/Blocs/air.png')
    air.viscosite = 0.0
    return air