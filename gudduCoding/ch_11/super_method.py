#  Super method ()

class Animals :
    def __init__ (self, a):
        self.legs = 4
        self.tail = 1
        self.face = 1
        self.domestic = True
        self.mammals = True

    def isMammals (self):
        if self.mammals :
            print("It is mammal")

    def isDomestic (self):
        if self.domestic:
            print("This is a Domestic animal")

class Dogs (Animals):
    def __init__(self):
        pass
    
    def __init__(self):
        super().isMammals()

    def __init__(self):
        super().__init__()
    
#  callind code.
tom = Dogs()
tom.isMammals()
tom.isDomestic()
tom.__init__()
