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

from crates.Default.crate import Crate

black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class Ball():

    Balls = []
    Frames = None

    def reset():
        Ball.Balls = []

    def setFrames(pygame):
        Ball.Frames = loadGIF("ball2.gif", pygame)

    def update(game, setUp):
        for ball in Ball.Balls:
            ball.move()
            ball.handleCollisions(game.width, game.height, game.barrect)
            if len(Ball.Balls) == 0:
                if game.score > game.highScore:
                    game.highScore = game.score
                game.finished = True
        
            for crate in Crate.Crates:
                    if ball.rect.colliderect(crate.rect):
                        crate.breakAction(game.pygame)
                        crate.hitByBall()
                        game.score += 1
                        game.scoreText = game.smallfont.render('Score: ' + str(game.score) , True , white)
                        ball.crateCollision(crate)
                        
                        if len(Crate.Crates) == 0:
                            game.currentSpeedMult += 0.1
                            game.score += 10
                            game.scoreText = game.smallfont.render('Score: ' + str(game.score) , True , white)
                            setUp(game.currentSpeedMult, game)

    def __init__(self, pygame, speed):
        self.image_index = 0
        self.sinceFrameChange = 0
        self.image = Ball.Frames[self.image_index]
        ballrect = self.image.get_rect()
        ballrect = ballrect.move(0, 600)
        self.rect = ballrect
        self.speed = [4 * speed, -4 * speed]
        Ball.Balls.append(self)

    def move(self):
        # adjust texture for animation
        if self.sinceFrameChange > 3:
            self.image_index += 1
            if self.image_index >= len(Ball.Frames):
                self.image_index = 0
            self.image = Ball.Frames[self.image_index]
            self.sinceFrameChange = 0
        else:
            self.sinceFrameChange += 1

        # move ball
        self.rect = self.rect.move(self.speed)
    
    def handleCollisions(self, width, height, barrect):

        # Remove ball below bar
        if self.rect.bottom > barrect.bottom:
            Ball.Balls.remove(self)

        # Edge collisions
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
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
