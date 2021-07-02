import pygame as pg
from . import Label, Button

class Color (Label.Label):

    def __init__(self, screen, address_img, x, y) :

        super().__init__(screen, address_img, x, y)

        self.color = {}
        self.num_color = [None]

        for r in [0,255] :
            for g in [0,255] :
                for b in [0,255] :
                    self.num_color.append( (r,g,b,255) )

        for i in range(1,5) :
            self.color[i] = Button.Button(screen, "color_" + str(i), 70 * i - 20, 425) 
            self.color[i+4] = Button.Button(screen, "color_" + str(i+4), 70 * i - 20 , 500)
            

    def blit(self) :

        self.screen.blit( self.image, self.rect.topleft)

        for i in range(1,9) :
            self.color[i].blit()


    def detect_press(self, mouse, position) :

        for i in range(1,9) :
            if self.color[i].detect_press(mouse, position) :
                return True, self.num_color[i]

        return False, None

