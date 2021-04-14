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

from utils.setUp import setUp

pygame.init()

pygame.display.set_caption('Ball Game')

size = width, height = 1200, 800

black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

highScore = 0


# defining a font
smallfont = pygame.font.SysFont('Corbel',35)

# rendering a text written in
# this font
scoreText = smallfont.render('Score: 0' , True , white)

screen = pygame.display.set_mode(size)

currentSpeedMult = 1
score = 0

clock = pygame.time.Clock()

barrect, bar, finished, crates = setUp(1, Ball, pygame)

# Game loop
while 1:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if not finished:

        if keys[pygame.K_LEFT] and barrect.x > 0:
                barrect = barrect.move(-10, 0)
        if keys[pygame.K_RIGHT] and (barrect.x + barrect.width) < width:
            barrect = barrect.move(10, 0)

        for index, ball in enumerate(Ball.Balls):
            if ball.rect.top + 2 > barrect.top:
                del Ball.Balls[index]
                
                if len(Ball.Balls) == 0:
                    if score > highScore:
                        highScore = score
                    finished = True

            ball.handleCollisions(width, height, barrect)

            for index, crate in enumerate(crates):
                if ball.rect.colliderect(crate.rect):
                    crates[index].breakAction(pygame)
                    del crates[index]
                    score += 1
                    scoreText = smallfont.render('Score: ' + str(score) , True , white)
                    ball.crateCollision(crate)
                    
                    if len(crates) == 0:
                        currentSpeedMult += 0.1
                        score += 10
                        scoreText = smallfont.render('Score: ' + str(score) , True , white)
                        barrect, bar, finished, crates = setUp(currentSpeedMult, Ball, pygame)

            screen.fill(black)
            for ball in Ball.Balls:
                screen.blit(ball.image, ball.rect)
            screen.blit(bar, barrect)
            for crate in crates:
                screen.blit(crate.image, crate.rect)
    else:
        screen.fill(green)
        currentSpeedMult = 1
        if keys[pygame.K_RETURN]:
            score = 0
            scoreText = smallfont.render('Score: 0' , True , white)
            barrect, bar, finished, crates = setUp(1, Ball, pygame)

        # Restart Text
        textRestart = smallfont.render('To restart the game press Return' , True , blue)
        screen.blit(textRestart , (width/2 - textRestart.get_width() / 2,height/2))

        #Current Score Text
        textCurrentScore = smallfont.render('You finished with a socre of ' + str(score) , True , white)
        screen.blit(textCurrentScore , (width/2 - textCurrentScore.get_width() / 2,height/2 + 50))

        ##High Score Text
        textHighScore = smallfont.render('Your high score in this session is ' + str(highScore) , True , black)
        screen.blit(textHighScore , (width/2 - textHighScore.get_width() / 2,height/2 + 100)) 


    screen.blit(scoreText , (width - 200,height - 50))


    pygame.display.flip()