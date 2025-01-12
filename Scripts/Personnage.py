import pygame

class Personnage():
    def __init__(self):
        self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")
        self.pos_indicator = pygame.image.load("Asset\image\personnage\pos_indicator.png")
        self.coordx = 448
        self.coordy = 256
        self.vie = 200
        self.armure = 0
        self.vitesse = 256
    
    def charger_sprite(self, chemin_sprite) -> pygame.surface.Surface:
        """Renvoi un sprite utilisable redimensionné en 64x128"""
        return pygame.transform.scale(pygame.image.load(chemin_sprite), (64, 128))

    def move(self, direction, collision_pos_bas,collision_pos_haut, delta):
        '''Permet d'exécuter les instructions nécessaires au déplacements du personnage'''
        if direction == "right":
            if collision_pos_bas == 0 and collision_pos_haut == 0 :
                self.coordx += self.vitesse * delta
                self.sprite = self.charger_sprite("Asset/image/personnage/skin de base droite.png")

        if direction == "left":
            if collision_pos_bas == 0 and collision_pos_haut == 0 :
                self.coordx -= self.vitesse * delta
                self.sprite = self.charger_sprite("Asset/image/personnage/skin de base gauche.png")

    def jump(self, bloc_grille):
        if bloc_grille == 0:
            self.coordy -= 128

    def gravité(self,bloc_grille):
        '''Applique la gravité au personnage en fonction des bloc en dessous'''
        if bloc_grille == 0  :
            self.coordy += 10

    def afficher(self, screen):
        '''Permet d'afficher le personnage sur l'écran'''
        screen.blit(self.sprite, (self.coordx - 32, self.coordy - 128))
        screen.blit(self.pos_indicator, (self.coordx, self.coordy)) #Pieds du joueur
        screen.blit(self.pos_indicator, (self.coordx, self.coordy - 140)) #Tête du joueur
        screen.blit(self.pos_indicator, (self.coordx - 32, self.coordy - 64)) #Bas gauche
        screen.blit(self.pos_indicator, (self.coordx + 32, self.coordy - 64)) #Bas droit
        screen.blit(self.pos_indicator, (self.coordx - 32, self.coordy - 128)) #Haut gauche
        screen.blit(self.pos_indicator, (self.coordx + 32, self.coordy - 128)) #Haut droit