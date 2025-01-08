import pygame

class Grille():
    def __init__(self, largeur:int, hauteur:int, taille_case:int,liste_initiale=None):
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.cases = liste_initiale

    def dessiner(self, surface:pygame.Surface):
        for ligne in range(len(self.cases)):
            for colonne in range(len(self.cases[ligne])):
                x = colonne * self.taille_case
                y = ligne * self.taille_case

        for x in range(0, self.largeur, self.taille_case):
            pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, self.hauteur))
        for y in range(0, self.hauteur, self.taille_case):
            pygame.draw.line(surface, (0, 0, 0), (0, y), (self.largeur, y))

class Bloc() :
    def __init__(self, chemin_sprite):
        self.sprite = self.charger_sprite(chemin_sprite)
        self.id = None

    def charger_sprite(self, chemin_sprite) -> pygame.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x64"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 64))

    def placer(self):
        """Place le bloc SUR la GRILLE au coordonées du curseur. """

    def detruire(self):
        """Notes pour plus tard :
            Si le bloc est solide --> mettre dans l'inventaire / détruire
            Si le bloc est liquide et que le joueur à un seau --> mettre dans le seau"""

class Solide(Bloc) :
    def __init__(self, id, chemin_sprite):
        super().__init__(chemin_sprite)
        self.durete : 0
        self.is_flammable = False
        self.has_collision = True

class Liquide(Bloc) : 
    def __init__(self, id, chemin_sprite):
        super().__init__()
        self.degats : 0
        self.viscosite : 0

def stone_block():
    '''Crée un bloc de pierre'''
    stone_block = Solide(1, 'Asset/image/Blocs/bloc_stone.png')
    stone_block.durete = 10
    return stone_block

def grass_block():
    '''Crée un bloc d'herbe'''
    grass_block = Solide(2, 'Asset/image/Blocs/bloc_herbe.png')
    grass_block.durete = 5
    return grass_block

def dirt_block():
    '''Crée un bloc de terre'''
    dirt_block = Solide(3, 'Asset/image/Blocs/bloc_terre.png')
    dirt_block.durete = 5
    return dirt_block

def air():
    '''Crée un bloc d'air'''
    air = Liquide(0, None)
    air.viscosite = 0.0
    return air
