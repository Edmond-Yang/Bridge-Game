import pygame as pg

class Background :

    def __init__(self, screen, num) :

        self.num = num 
        self.alpha = 255

        self.screen = screen
        self.state_move = False

        self.image = pg.image.load("./Photo/background_" + str(num) + ".png")
        self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.topleft = (self.screen.get_width(), self.screen.get_height() // 2 - self.image.get_height() // 2 - 50)


    def move(self, dx = -5, dy = 0) :

        x, y = self.rect.topleft
        x += dx
        self.state_move = True

        self.rect.topleft = (x, y)


    def reset(self) :
        self.state_move = False
        self.rect.topleft = (self.screen.get_width(), self.screen.get_height() // 2 - self.image.get_height() // 2 - 50 )


    def blit(self) :
        self.screen.blit(self.image,  self.rect.topleft)

    def get_Left(self) :
        return self.rect.left

    def get_Width(self) :
        return self.image.get_width()