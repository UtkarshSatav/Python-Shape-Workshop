class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def curvedSurfaceArea(self):
        return 2 * 3.14 * self.radius * self.height