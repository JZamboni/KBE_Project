from __future__ import division
from parapy.geom import *
from parapy.core import *
from math import *
from Tkinter import *
from tkMessageBox import *


class Fuselage(GeomBase):
    """
    Basic class Fuselage
    """

    @Input
    def fuselagLength(self):
        """
        Aircraft fuselage length
        :Unit: [m]
        :rtype: float
        """
        return 35.

    @Input
    def fuselageDiameter(self):
        """
        Aircraft Diameter
        :Unit: [m]
        :rtype: float
        """
        return 4.

    @Input
    def noseSlenderness(self):
        """
        Aircraft Diameter
        :Unit: [m]
        :rtype: float
        """
        return 4.


if __name__ == '__main__':
    from parapy.gui import display

    obj = Fuselage()
    display(obj)