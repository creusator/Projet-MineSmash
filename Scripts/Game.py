class Bloc() :
    def __init__(self):
        self.sprite = None
    
    def placer(self):
        pass
    
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