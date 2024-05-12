

class Closet(object):
    has_legs = True
    def __init__(self, color:str, height:int, width:int):
        self.color = color
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def set_shelf(self, length, width):
        self.shelf = Build_shelf(length, width)

class Build_shelf(object):
    def __init__(self, color, thickness):
        self.color = color
        self.thickiness = thickness

    def get_area(self):
        return


design1 = Closet("brown", 10, 5)
print(design1.get_surface())
print(design1.has_legs)
design1_shelf = design1.set_shelf("blue", 2)