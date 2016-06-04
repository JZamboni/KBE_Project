from parapy.core import *
from parapy.gui import *
from parapy.geom import *
from ComponentEx.fuselageEx import FuselageEx

class AirplaneEx(Base):

    @Part
    def cylinder(self):
        return FuselageEx()

if __name__ == '__main__':
    from parapy.gui import display
    obj = AirplaneEx()
    display(obj)