from random import seed
from random import random
seed(1)

WHITE=(255,255,255)
BLUE=(0,0,255)

from crates.Default.crate import Default
from crates.AddBall.crate import AddBall

# Set up game
def setUp(speed, Ball, pygame):
    finished = False
    crates = []
    Ball.reset()
    Ball.setFrames(pygame)
    Ball(pygame, speed)

    bar = pygame.image.load("bar.png")
    barrect = bar.get_rect()


    for row in range(3):
        for num in range(10):
            ranNum = random()
            if ranNum < 0.05:
                crates.append(AddBall(pygame, row, num))
            else:
                crates.append(Default(pygame, row, num))

    barrect = barrect.move((200, 700))

    return barrect, bar, finished, crates