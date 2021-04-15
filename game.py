#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      m.kazimierczak
#
# Created:     03/03/2021
# Copyright:   (c) m.kazimierczak 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, pygame


from Ball import Ball
from crates.Default.crate import Crate

from utils.setUp import setUp


black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class Game():

    def __init__(self):

        # init pygame and set screen
        self.pygame = pygame
        self.pygame.init()
        self.pygame.display.set_caption('Ball Game')
        self.screenSize = self.width, self.height = 1200, 800
        self.screen = self.pygame.display.set_mode(self.screenSize)


        # Defining variables
        self.highScore = 0
        self.currentSpeedMult = 1
        self.score = 0
        self.smallfont = self.pygame.font.SysFont('Corbel',35)
        self.scoreText = self.smallfont.render('Score: 0' , True , white)

        # Set up game clock
        self.clock = self.pygame.time.Clock()

        # finish setting up game
        setUp(1, self)
    

    def iteration(self):

        self.inputAndEvents()
        Ball.update(self, setUp)

    
    def inputAndEvents(self):

        # Handle pressed keys
        self.keys = self.pygame.key.get_pressed()
        if not self.finished:
            if self.keys[self.pygame.K_LEFT] and self.barrect.x > 0:
                self.barrect = self.barrect.move(-10, 0)
            if self.keys[self.pygame.K_RIGHT] and (self.barrect.x + self.barrect.width) < self.width:
                self.barrect = self.barrect.move(10, 0)

        # Handle game events
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT: sys.exit()

        
    def draw(self):
        if not self.finished:
            self.screen.fill(black)
            self.screen.blit(self.scoreText , (self.width - 200,self.height - 50))
            for ball in Ball.Balls:
                self.screen.blit(ball.image, ball.rect)
            self.screen.blit(self.bar, self.barrect)
            for crate in Crate.Crates:
                self.screen.blit(crate.image, crate.rect)
        else:
            self.screen.fill(green)
            self.currentSpeedMult = 1
            if self.keys[self.pygame.K_RETURN]:
                self.score = 0
                self.scoreText = self.smallfont.render('Score: 0' , True , white)
                setUp(1, self)

            # Restart Text
            self.textRestart = self.smallfont.render('To restart the game press Return' , True , blue)
            self.screen.blit(self.textRestart , (self.width/2 - self.textRestart.get_width() / 2, self.height/2))

            #Current Score Text
            textCurrentScore = self.smallfont.render('You finished with a socre of ' + str(self.score) , True , white)
            self.screen.blit(textCurrentScore , (self.width/2 - textCurrentScore.get_width() / 2,self.height/2 + 50))

            # High Score Text
            textHighScore = self.smallfont.render('Your high score in this session is ' + str(self.highScore) , True , black)
            self.screen.blit(textHighScore , (self.width/2 - textHighScore.get_width() / 2,self.height/2 + 100)) 

        self.pygame.display.flip()


    def loop(self):
        while True:
            self.iteration()
            self.draw()
            self.clock.tick(60)