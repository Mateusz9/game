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
pygame.init()

size = width, height = 1200, 800
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

bar = pygame.image.load("bar.png")
barrect = bar.get_rect()

barrect = barrect.move((200, 700))

frames_since_bounce = 0

while 1:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and barrect.x > 0:
        barrect = barrect.move(-10, 0)
    if keys[pygame.K_RIGHT] and (barrect.x + barrect.width) < width:
        barrect = barrect.move(10, 0)

    print(ballrect.x + barrect.width)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width  and frames_since_bounce > 100:
        speed[0] = -speed[0]
        frames_since_bounce = 0
    if ballrect.top < 0 or ballrect.bottom > height  and frames_since_bounce > 100:
        speed[1] = -speed[1]
        frames_since_bounce = 0
    frames_since_bounce += 1

    if ballrect.colliderect(barrect):
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(bar, barrect)
    pygame.display.flip()
    pygame.time.delay(10)