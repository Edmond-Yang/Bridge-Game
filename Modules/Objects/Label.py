import pygame as pg

class Label :

    def __init__(self, screen, address_img, x, y) :

        self.screen = screen 
        
        self.image = pg.image.load("./Photo/label_" + address_img + ".png" )

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    def blit(self) :
        self.screen.blit( self.image, self.rect.topleft)