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

from utils.getFrames import loadGIF

class Ball():

    Balls = []
    Frames = None

    def reset():
        Ball.Balls = []

    def setFrames(pygame):
        Ball.Frames = loadGIF("ball2.gif", pygame)

    def __init__(self, pygame, speed):
        self.image_index = 0
        self.sinceFrameChange = 0
        self.image = Ball.Frames[self.image_index]
        ballrect = self.image.get_rect()
        ballrect = ballrect.move(0, 650)
        self.rect = ballrect
        self.speed = [4 * speed, -4 * speed]
        Ball.Balls.append(self)

    def move(self):
        if self.sinceFrameChange > 3:
            self.image_index += 1
            if self.image_index >= len(Ball.Frames):
                self.image_index = 0
            self.image = Ball.Frames[self.image_index]
            self.sinceFrameChange = 0
        else:
            self.sinceFrameChange += 1
        self.rect = self.rect.move(self.speed)
    
    def handleCollisions(self, width, height, barrect):

        # Edge collisions
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
            frames_since_bounce = 0
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
        
        # Collisions with bar
        if self.rect.colliderect(barrect):
            if (self.rect.bottom) > barrect.top:
                overlap = self.rect.bottom - barrect.top + 10
                self.rect.top -= overlap
                self.speed[1] = -self.speed[1]
            
        for ball in Ball.Balls:
            if self != ball:
                if self.rect.colliderect(ball.rect):
                    self.speed[0] = -self.speed[0]
                    ball.speed[0] = -ball.speed[0]
        
    def crateCollision(self, crate):
        if (self.rect.top) < crate.rect.bottom - 10:
            self.speed[0] = -self.speed[0]
        else:
            self.speed[1] = -self.speed[1]
