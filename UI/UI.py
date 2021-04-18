import pygame

black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

class UI():

    def __init__(self):
        # Load font
        self.smallfont = pygame.font.SysFont('Corbel',35)

        #Load Bottom Bar
        self.woodenBar = pygame.image.load("UI/assets/wood.png").convert_alpha()
        # print(self.woodenBar.get_at((0,0)))
        # self.woodenBar.set_colorkey((255, 0, 255), pygame.RLEACCEL)

    def draw(self, game):

        if not game.finished:
            game.screen.blit(self.woodenBar, (game.width - self.woodenBar.get_width(), game.height - self.woodenBar.get_height() + 80))
            self.scoreText = self.smallfont.render(f'Score: {str(game.score)}' , True , white)
            game.screen.blit(self.scoreText , (game.width - 200,game.height - 50))
        else:
            # Restart Text
            textRestart = self.smallfont.render('To restart the game press Return' , True , blue)
            game.screen.blit(textRestart , (game.width/2 - textRestart.get_width() / 2, game.height/2))

            #Current Score Text
            textCurrentScore = self.smallfont.render('You finished with a socre of ' + str(game.score) , True , white)
            game.screen.blit(textCurrentScore , (game.width/2 - textCurrentScore.get_width() / 2,game.height/2 + 50))

            # High Score Text
            textHighScore = self.smallfont.render('Your high score in this session is ' + str(game.highScore) , True , black)
            game.screen.blit(textHighScore , (game.width/2 - textHighScore.get_width() / 2, game.height/2 + 100)) 

    def listenForInput(self, game):
        pass
