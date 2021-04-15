#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m.kazimierczak
#
# Created:     14/04/2021
# Copyright:   (c) m.kazimierczak 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Ball import Ball
from crates.Default.crate import Crate

class AddBallCrate(Crate):

    def __init__(self, pygame, row, num):
        super(AddBallCrate, self).__init__(pygame, row, num, "crates/images/AddBall.png")