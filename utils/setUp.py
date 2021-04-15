from random import seed
from random import random
seed(1)

WHITE=(255,255,255)
BLUE=(0,0,255)

from crates.Default.crate import Crate
from crates.AddBall.crate import AddBallCrate

from Ball import Ball

# Set up game
def setUp(speed, game):
    print("Setting up game")
    Ball.reset()
    Ball.setFrames(game.pygame)
    Ball(game.pygame, speed)

    bar = game.pygame.image.load("bar.png")
    barrect = bar.get_rect()


    for row in range(3):
        for col in range(10):
            ranNum = random()
            if ranNum < 0.05:
                AddBallCrate(game.pygame, row, col)
            else:
                Crate(game.pygame, row, col)

    barrect = barrect.move((200, 700))

    game.finished = False

    game.barrect = barrect
    game.bar = bar