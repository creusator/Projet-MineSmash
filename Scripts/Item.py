import pygame


class Item():
    def __init__(self, chemin_sprite:str):
        self.sprite = self.charger_sprite(chemin_sprite)

    def charger_sprite(self, chemin_sprite:str) -> pygame.Surface:
        """Renvoi un sprite utilisable redimensionné en 16*16"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (16, 16))


class Bloc(Item):
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)

class Outil(Item):
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)

class Nourriture(Item):
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)
