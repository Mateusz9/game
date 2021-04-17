from random import seed
from random import random
seed(1)

WHITE=(255,255,255)
BLUE=(0,0,255)

from crates.Default.crate import Crate
from crates.AddBall.crate import AddBallCrate
from crates.Bomb.crate import BombCrate

from Ball import Ball

# Set up game
def setUp(speed, game):
    Ball.reset()
    Ball(speed)

    bar = game.pygame.image.load("bar.png")
    barrect = bar.get_rect()


    for row in range(3):
        for col in range(10):
            ranNum = random()
            if ranNum < 0.01:
                AddBallCrate(row, col)
            elif ranNum < 0.1:
                BombCrate(row, col)
            else:
                Crate(row, col)

    barrect = barrect.move((200, 700))

    game.finished = False

    game.barrect = barrect
    game.bar = bar
