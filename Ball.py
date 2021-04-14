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
    
    def handleCollisions(self, width, height, barrect):

        # Edge collisions
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
            frames_since_bounce = 0
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
        
        # Collisions with bar
        if self.rect.colliderect(barrect):
            if (self.rect.top + self.rect.height) > barrect.top + 2:
                self.speed[0] = -self.speed[0]
            else:
                self.speed[1] = -self.speed[1]
        
    def crateCollision(self, crate):
        if (self.rect.top) < crate.rect.top + 2:
            self.speed[1] = -self.speed[1]
            self.speed[0] = -self.speed[0]
        else:
            self.speed[1] = -self.speed[1]
