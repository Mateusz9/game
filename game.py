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

from crates.Default.crate import Default
from crates.AddBall.crate import AddBall

from Ball import Ball

from random import seed
from random import random
# seed random number generator
seed(1)

pygame.init()

pygame.display.set_caption('Ball Game')

def setUp():
    pass

size = width, height = 1200, 800
black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)



# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
text = smallfont.render('To restart the game press Return' , True , blue)
scoreText = smallfont.render('Score: 0' , True , white)

screen = pygame.display.set_mode(size)

currentSpeedMult = 1
score = 0

def setUp(speed):
    finished = False
    crates = []
    balls = [Ball(pygame, speed)]
    ball = pygame.image.load("intro_ball.gif")
    ball = pygame.transform.scale(ball, (100, 100))
    ballrect = ball.get_rect()

    speed = [6 * speed, -6 * speed]

    ballrect = ballrect.move(0, 650)

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

    return balls, barrect, bar, finished, crates

balls, barrect, bar, finished, crates = setUp(1)

while 1:
    pygame.time.delay(10)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if not finished:
        for ball in balls:
            if ball.rect.top + 2 > ball.rect.top:
                score = 0
                scoreText = smallfont.render('Score: 0' , True , white)
                screen.fill(green)


            if keys[pygame.K_LEFT] and barrect.x > 0:
                barrect = barrect.move(-10, 0)
            if keys[pygame.K_RIGHT] and (ball.rect.x + barrect.width) < width:
                barrect = barrect.move(10, 0)


            ball.rect = ball.rect.move(ball.speed)
            if ball.rect.left < 0 or ball.rect.right > width:
                ball.speed[0] = -ball.speed[0]
                frames_since_bounce = 0
            if ball.rect.top < 0 or ball.rect.bottom > height:
                ball.speed[1] = -ball.speed[1]

            if ball.rect.colliderect(barrect):
                if (ball.rect.top + ball.rect.height) > barrect.top + 2:
                    ball.speed[0] = -ball.speed[0]
                else:
                    ball.speed[1] = -ball.speed[1]

            for index, crate in enumerate(crates):
                if ball.rect.colliderect(crate.rect):
                    crates[index].breakAction()
                    del crates[index]
                    score += 1
                    scoreText = smallfont.render('Score: ' + str(score) , True , white)
                    if (ball.rect.top) < crate.rect.top + 2:
                        ball.speed[1] = -ball.speed[1]
                        ball.speed[0] = -ball.speed[0]
                    else:
                        ball.speed[1] = -ball.speed[1]
                    if len(crates) == 0:
                        currentSpeedMult += 0.1
                        score += 10
                        scoreText = smallfont.render('Score: ' + str(score) , True , white)
                        balls, barrect, bar, finished, crates = setUp(currentSpeedMult)


    if not finished:
        screen.fill(black)
        for ball in balls:
            screen.blit(ball.image, ball.rect)
        screen.blit(bar, barrect)
        for crate in crates:
            screen.blit(crate.image, crate.rect)
    else:
        currentSpeedMult = 1
        if keys[pygame.K_RETURN]:
            balls, barrect, bar, finished, crates = setUp(1)
        screen.blit(text , (width/2+50,height/2))


    screen.blit(scoreText , (width - 200,height - 50))


    pygame.display.flip()