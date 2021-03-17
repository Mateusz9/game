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

pygame.display.set_caption('Ball Game')



size = width, height = 1200, 800
speed = [8, -8]
black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.font.init()
finished = False
font = pygame.font.SysFont(None, 24)
img = font.render('hello', True, blue)


crates = []

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ball = pygame.transform.scale(ball, (100, 100))
ballrect = ball.get_rect()

ballrect = ballrect.move(0, 650)

bar = pygame.image.load("bar.png")
barrect = bar.get_rect()

for row in range(1):
    for num in range(10):
        crateImg = pygame.image.load("crate.png")
        crateImg = pygame.transform.scale(crateImg, (100, 100))
        craterect = crateImg.get_rect()
        craterect = craterect.move(110 * num + 50, 10 + row * 110)
        crates.append([crateImg, craterect])

barrect = barrect.move((200, 700))


while 1:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and barrect.x > 0:
        barrect = barrect.move(-10, 0)
    if keys[pygame.K_RIGHT] and (barrect.x + barrect.width) < width:
        barrect = barrect.move(10, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        frames_since_bounce = 0
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if ballrect.colliderect(barrect):
        if (ballrect.top + ballrect.height) > barrect.top + 2:
            speed[0] = -speed[0]
        else:
            speed[1] = -speed[1]

    for index, crate in enumerate(crates):
        if ballrect.colliderect(crate[1]):
            del crates[index]
            if (ballrect.top) < crate[1].top + 2:
                speed[1] = -speed[1]
                speed[0] = -speed[0]
            else:
                speed[1] = -speed[1]
            if len(crates) == 0:
                finished = True
                textsurface = myfont.render('Has ganado', False, (0, 0, 0))

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(bar, barrect)
    for crate in crates:
        screen.blit(crate[0], crate[1])
    pygame.display.flip()

    if 1:
        screen.blit(img, (20, 20))
    pygame.time.delay(10)