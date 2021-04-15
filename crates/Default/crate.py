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

    def removeNearby(row, col):
        counter = 0
        print(len(Crate.Crates))
        for crate in Crate.Crates:
            counter += 1
            if abs(row - crate.row) == 1 and abs(col - crate.col) == 1:
                crate.hitByBall()
        print(counter)

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

        self.pygame = pygame

        Crate.Crates.append(self)


    def hitByBall(self):
        Crate.Crates.remove(self)