class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def curvedSurfaceArea(self):
        return 2 * 3.14 * self.radius * self.height

      def surface_area(self):
        return 2*3.14*self.radius*self.height+2*3.14*(self.radius**2)
      
    def height(self):
        return self.height
      
    def volume(self):
        return 3.14 * self.radius ** 2 * self.height 