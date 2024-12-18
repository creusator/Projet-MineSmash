class Bloc() :
    def __init__(self):
        self.sprite = None

class Solide(Bloc) :
    def __init__(self):
        super.__init__()
        self.durete : 0
        self.is_flammable = False

class Liquide(Bloc) : 
    def __init__(self):
        super.__init__()
        self.damage : 0
        self.viscosity : 0