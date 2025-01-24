class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def height(self):
        return self.height
    def volume(self):
        return 3.14 * self.radius ** 2 * self.height 