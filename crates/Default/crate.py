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

class Crate():

    Crates = []

    def __init__(self, pygame, row, col, texturePath = "crates/images/Default.png"):

        # Load texture from image
        self.image = pygame.image.load(texturePath)
        self.image = pygame.transform.scale(self.image, (100, 100))

        # Position crate on screen
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(110 * col + 50, 10 + row * 110)

        # store the row and column of this crate
        self.row = row
        self.col = col

        Crate.Crates.append(self)

    def breakAction(self, pygame):
        pass

    def hitByBall(self):
        Crate.Crates.remove(self)