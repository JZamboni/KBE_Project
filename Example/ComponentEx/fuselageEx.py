from parapy.core import *
from parapy.geom import *
from Example.importerEx import ImporterEx

class FuselageEx(Base):

    @Input
    def fuselageLengthEx(self):
        return ImporterEx.fuselageLength

    @Input
    def radiusEx(self):
        return ImporterEx.fuselageRadius

    @Part
    def cylinderEx(self):
        return Cylinder(radius = self.radiusEx, height = self.fuselageLengthEx)

if __name__ == '__main__':
    from parapy.gui import display
    obj = FuselageEx()
    display(obj)