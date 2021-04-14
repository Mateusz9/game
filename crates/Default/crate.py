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

class Default():

    def __init__(self, pygame, row, num):
        crateImg = pygame.image.load("crates/images/Default.png")
        crateImg = pygame.transform.scale(crateImg, (100, 100))
        craterect = crateImg.get_rect()
        craterect = craterect.move(110 * num + 50, 10 + row * 110)

        self.image = crateImg
        self.rect = craterect

    def breakAction(self, pygame):
        pass