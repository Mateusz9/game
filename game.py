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
    ball = pygame.image.load("intro_ball.gif")
    ball = pygame.transform.scale(ball, (100, 100))
    ballrect = ball.get_rect()

    speed = [6 * speed, -6 * speed]

    ballrect = ballrect.move(0, 650)

    bar = pygame.image.load("bar.png")
    barrect = bar.get_rect()

    for row in range(3):
        for num in range(10):
            crateImg = pygame.image.load("crate.png")
            crateImg = pygame.transform.scale(crateImg, (100, 100))
            craterect = crateImg.get_rect()
            craterect = craterect.move(110 * num + 50, 10 + row * 110)
            crates.append([crateImg, craterect])

    barrect = barrect.move((200, 700))

    return ballrect, ball, barrect, bar, finished, crates, speed

ballrect, ball, barrect, bar, finished, crates, speed = setUp(1)

while 1:
    pygame.time.delay(10)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if not finished:
        if ballrect.top + 2 > barrect.top:
            score = 0
            scoreText = smallfont.render('Score: 0' , True , white)
            screen.fill(green)
            finished = True

        if keys[pygame.K_LEFT] and barrect.x > 0:
            barrect = barrect.move(-10, 0)
        if keys[pygame.K_RIGHT] and (barrect.x + barrect.width) < width:
            barrect = barrect.move(10, 0)


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
                    currentSpeedMult += 0.1
                    score += 1
                    scoreText = smallfont.render('Score: ' + str(score) , True , white)
                    ballrect, ball, barrect, bar, finished, crates, speed = setUp(currentSpeedMult)

    if not finished:
        screen.fill(black)
        screen.blit(ball, ballrect)
        screen.blit(bar, barrect)
        for crate in crates:
            screen.blit(crate[0], crate[1])
    else:
        currentSpeedMult = 1
        if keys[pygame.K_RETURN]:
            ballrect, ball, barrect, bar, finished, crates, speed = setUp(1)
        screen.blit(text , (width/2+50,height/2))
    screen.blit(scoreText , (width - 200,height - 50))



    pygame.display.flip()