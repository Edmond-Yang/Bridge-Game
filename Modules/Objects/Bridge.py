import pygame as pg

class Bridge :

    def __init__(self, screen, color) :

        self.screen = screen
        self.limit = 320

        self.color = color

        self.reset()
        

    def lengthen(self) :

        if self.length >= self.limit :
            self.length = 5
            return 

        self.length += 5 

        self.end_point = pg.Vector2(0, -self.length)
        

    def detect_Press(self, mouse) :

        if self.rotated :
            return True

        elif self.unpressed and self.pressed :

            if self.rotating(3) :
                self.rotated = True

        elif mouse[0] :

            self.lengthen()
            self.pressed = True
            self.unpressed = False

        else :
            self.unpressed = True

        return False


    def rotating(self, angle) :

        self.angle += angle

        return self.angle == 90


    def blit(self) :
        pg.draw.line(self.screen, self.color, self.start_point, self.start_point + self.end_point.rotate(self.angle), 3)


    def reset(self) :

        self.angle = 0
        self.length = 5
    
        self.start_point = pg.Vector2(27, 520)
        self.end_point = pg.Vector2(0, -self.length)

        self.pressed = False
        self.unpressed = False
        self.rotated = False


    def get_Length(self) :
        return self.length
