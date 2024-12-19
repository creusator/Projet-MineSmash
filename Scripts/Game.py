class Bloc() :
    def __init__(self):
        self.sprite = None
        self.nom = None
    
    def placer(self):
        pass

    def detruire(self):
        """Notes pour plus tard :
            Si le bloc est solide --> détruire
            Si le bloc est liquide et que le joueur à un seau --> mettre dans le seau"""
    
class Solide(Bloc) :
    def __init__(self):
        super.__init__()
        self.durete : 0
        self.is_flammable = False

class Liquide(Bloc) : 
    def __init__(self):
        super.__init__()
        self.degats : 0
        self.viscosite : 0

class Personnage():
    def __init__(self):
        self.coordonées = [x, y]
        self.vie = 200
        self.armure = 0
        self.vitesse = 10
