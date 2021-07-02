import pygame as pg

class Button :

    def __init__ (self, screen, address_img, x, y) :

        self.screen = screen
        self.state_press = False
        self.state_click = False

        self.image_1 = pg.image.load("./Photo/button_" + address_img + "_1.png" )
        self.image_1.convert()

        self.image_2 = pg.image.load("./Photo/button_" + address_img + "_2.png" )
        self.image_2.convert()

        self.rect = self.image_1.get_rect()
        self.rect.topleft = (x, y)
        

    def detect_press (self, mouse, position_mouse) :

        x, y = position_mouse

        if mouse[0] :

            self.state_press = True

            if x >= self.rect.left and x <= self.rect.right and y >= self.rect.top and y <= self.rect.bottom :
                self.state_click = True
        else :
            self.state_click = False

        if mouse[0] or not self.state_press :
            return False

        self.state_press = False
        
        if x <= self.rect.left or x >= self.rect.right :
            return False

        if y <= self.rect.top or y >= self.rect.bottom :
            return False

        return True


    def blit(self) :

        if not self.state_click :
            self.screen.blit(self.image_1, self.rect.topleft)
        else :
            self.screen.blit(self.image_2, self.rect.topleft)
