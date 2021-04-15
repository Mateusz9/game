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

    Balls = []

    def reset():
        Ball.Balls = []

    def __init__(self, pygame, speed):
        ball = pygame.image.load("intro_ball.gif")
        ball = pygame.transform.scale(ball, (100, 100))
        ballrect = ball.get_rect()
        ballrect = ballrect.move(0, 650)
        self.image = ball
        self.rect = ballrect
        self.speed = [4 * speed, -4 * speed]
        Ball.Balls.append(self)

    def move(self):
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
        print("self: " + str(self.rect.top), "  crate: " + str(crate.rect.bottom) )
        if (self.rect.top) < crate.rect.bottom - 10:
            self.speed[0] = -self.speed[0]
        else:
            self.speed[1] = -self.speed[1]
