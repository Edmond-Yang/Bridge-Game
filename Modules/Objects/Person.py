import pygame as pg

class Person :

    def __init__ (self, screen):
        
        self.screen = screen
        self.reset()
            

    def move (self, dx = 5, dy = 0) :
        
        x, y = self.rect.topleft
       
        x += dx
        y += dy

        self.rect.topleft = (x, y)


    def blit(self) :

        if self.state == "Running" or self.state == "Moving" or self.state == "Walking" :

            if self.num_change == 15  :
                self.num_change = 0
                self.num = self.num + 1 if self.num < 4 else 1

            else :
                self.num_change += 1
                self.num = 1 if self.num > 5 else self.num

        elif self.state == "Making" :

            if self.num_change == 15  :
                self.num_change = 0
                self.num = self.num + 1 if self.num < 6 else 5

            else :
                self.num_change += 1
                self.num = 5 if self.num < 5 or self.num == 7 else self.num

        elif  self.state == "Falling" :

            if self.times == 0 :

                if self.rect.top < self.screen.get_height() :
                    
                    self.num = 7
                    self.move(dx = 0, dy = 7)
                else :
                    self.times  += 1

            elif self.times == 1 :

                if self.rect.top > self.screen.get_height() - 150 :
                    self.num = 8
                    self.move(dx = 0, dy = -4)
                else :
                    self.times  += 1

            elif self.times == 2 :
    
                if self.rect.top < self.screen.get_height() :
                    self.num = 8
                    self.move(dx = 0, dy = 5)
                else :
                    return True
        
        else :
            print("Something Wrong with person status " + self.person.get_Status()  + "!")

        self.screen.blit( self.image[self.num] , self.rect.topleft )

        return False


    def get_Status(self) :
        return self.state

    def set_Status(self, var) :
        self.state = var

    def get_Left(self) :
        return self.rect.left

    def get_Right(self) :
        return self.rect.right

    def get_Gravity(self) :
        return int(self.image[self.num].get_width() * 0.15) 

    def set_Position(self, x, y) :
        self.rect.topleft = (x, y)

    def reset(self) :

        self.num = 1

        self.num_change = 0
        self.times = 0

        self.state = "Making"

        self.image = { i : pg.image.load("./Photo/new_icon_" + str(i) + ".png" ) for i in range(1,9) }

        self.rect = self.image[1].get_rect()
        self.rect.bottomleft = (5 , 520 )
