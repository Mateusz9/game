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

class Ball():

    def __init__(self, pygame, speed):
        ball = pygame.image.load("intro_ball.gif")
        ball = pygame.transform.scale(ball, (100, 100))
        ballrect = ball.get_rect()
        ballrect = ballrect.move(0, 650)
        self.image = ball
        self.rect = ballrect
        self.speed = [6 * speed, -6 * speed]
