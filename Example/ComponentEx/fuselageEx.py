from parapy.core import *
from parapy.geom import *

class FuselageEx(Base):

    @Input
    def fuselageLengthEx(self):
        return 30.0

    @Input
    def radiusEx(self):
        return 5.0

    @Part
    def cylinderEx(self):
        return Cylinder(radius = self.radiusEx, height = self.fuselageLengthEx)

if __name__ == '__main__':
    from parapy.gui import display
    obj = FuselageEx()
    display(obj)