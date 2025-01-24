class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2*3.14*self.radius*self.height+2*3.14*(self.radius**2)
