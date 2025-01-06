class Personnage():
    def __init__(self):
        self.coordx = 0
        self.coordy = 0
        self.vie = 200
        self.armure = 0
        self.vitesse = 10
    
    def move(self, arg):
        if arg == "right":
            self.coordx += 5

        if arg == "left":
            self.coordx -= 5
        
        if arg == "jump":
            coordy += 10 
        #Multiplier 10 par la viscosité du liquide dans lequel est le joueur.