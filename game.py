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
from crates.Bomb.crate import BombCrate
from UI.UI import UI

from utils.setUp import setUp
from utils.Background.Background import Background


black = 0, 0, 0
white = (255, 255, 255)
green = (119, 170, 119)
blue = (0, 0, 128)



class Game():

    def __init__(self):

        # init pygame and set screen
        self.pygame = pygame
        self.pygame.init()
        self.pygame.display.set_caption('Ball Game')
        self.screenSize = self.width, self.height = 1200, 850
        self.screen = self.pygame.display.set_mode(self.screenSize)

        # Defining variables
        self.highScore = 0
        self.currentSpeedMult = 1
        self.score = 0
        self.paused = False

        # Initialize animations
        Ball.setFrames()
        BombCrate.setFrames()
        self.background = Background()

        # Initialize UI class
        self.ui = UI(self)
        

        # Set up game clock
        self.clock = pygame.time.Clock()

        # finish setting up game
        setUp(1, self)
    

    def iteration(self):

        self.inputAndEvents()
        
        if not self.paused:
            Ball.update(self, setUp)

    
    def inputAndEvents(self):

        # Handle pressed keys
        self.keys = pygame.key.get_pressed()
        events = pygame.event.get()
        mous_pos = pygame.mouse.get_pos()

        if not self.finished and not self.paused:
            self.bar.move(self.keys, self.width)

        # Handle game events
        for event in events:
            if event.type == pygame.QUIT: sys.exit()

        self.ui.listenForInput(self.keys, self, events, mous_pos)

        
    def draw(self):
        if not self.finished:

            self.screen.fill(green)
            self.background.draw(self)

            # Render entities
            for ball in Ball.Balls:
                self.screen.blit(ball.image, ball.rect)

            self.bar.draw(self.screen)
            Crate.drawCrates(self.screen)
                
        else:
            # If game is finished
            self.screen.fill(green)
            if self.keys[self.pygame.K_RETURN]:
                self.currentSpeedMult = 1
                self.score = 0
                setUp(1, self)

            

        self.ui.draw(self)
        self.pygame.display.flip()


    def loop(self):
        while True:
            self.iteration()
            self.draw()
            self.clock.tick(60)