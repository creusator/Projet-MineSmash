import pygame


class Item():
    """
    Classe qui va être utilisé sur les autres
    classes de item.py pour des chose à 
    utilisé de manière répété
    """
    def __init__(self, chemin_sprite:str):
        self.sprite = self.charger_sprite(chemin_sprite)
        self.stack = 0

    def charger_sprite(self, chemin_sprite:str) -> pygame.Surface:
        """Renvoi un sprite utilisable redimensionné en 16*16"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (16, 16))


class Bloc(Item):
    """
    Classe qui va permettre de réaliser un bloc/item
    qui aura la possiblité de se faire poser    
    """
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)
        self.poser = None

class Outil(Item):
    """
    Classe qui permet d'avoir des outils/item
    qui auront une durabilité, un usage(bois,pierre,terre)
    et une efficacité (bois,pierre,fer,diamant,obsidienne)
    """
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)
        self.durabilite = 0
        self.usage = None
        self.efficacite = None

class Nourriture(Item):
    """
    Classe qui permet d'avoir de la nourriture/item
    qui auront l'utilité de faire consommer et
    régénerer de la vie
    """
    def __init__(self, chemin_sprite:str):
        super().__init__(chemin_sprite)
        self.regeneration = 0

def identify_item(item_id:int):
    '''Retourne un item ainsi que tout ces attributs en fonction d'un id'''
    if item_id == 0 :
        return air_block_item()
    if item_id == 1 :
        return stone_block_item()
    if item_id == 2 :
        return grass_block_item()
    if item_id == 3 :
        return dirt_block_item()


def stone_block_item() -> Bloc:
    '''Crée un item de bloc de pierre'''
    stone_block = Solide('Asset/image/Blocs/bloc_stone.png')
    return stone_block_item

def grass_block_item() -> Bloc:
    '''Crée un item de bloc d'herbe'''
    stone_block = Bloc('Asset/image/Blocs/bloc_herbe.png')
    return grass_block_item

def dirt_block_item() -> Bloc:
    '''Crée un item de bloc de terre'''
    stone_block = Bloc('Asset/image/Blocs/bloc_terre.png')
    return dirt_block_item

def air_block_item() -> Bloc:
    '''Crée un item de bloc d'air'''
    stone_block = Bloc('Asset/image/Blocs/air.png')
    return air_block_item