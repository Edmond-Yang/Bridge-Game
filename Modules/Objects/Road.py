# -*- coding: utf-8 -*-
import pygame as pg
import random

class Road :

    def __init__(self, screen, table_prob, number = 0, x = 0, y = 640) :

        self.screen = screen
        number = random.choices([ i  for i in range(1,9) ], table_prob)[0] if number == 0 else number
        
        
        self.image = pg.image.load("./Photo/road_" + str(number) + ".png")
        self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        
        self.state = True
        self.speed = 0
        self.direction = 0;#0 left ,1 right

    def move (self, dx = -5, dy = 0) :
    
        x, y = self.rect.topleft

        x += dx
        y += dy

        self.rect.topleft = (x, y)
        
    def Keep_Moving(self,speed):
        self.speed = speed + 1
        x, y = self.rect.topleft
        limit = 330-self.image.get_width()
        
        if self.direction == 0:
            if x > 70 :
                x -= self.speed
            elif x <= 70:
                self.direction = 1
        else:
            if x < limit:
                x += self.speed  
            elif x >= limit:
                self.direction = 0
        if self.state:
            self.blit()

        self.rect.topleft = (x, y)

    def blit(self) :
        self.screen.blit(self.image, self.rect.topleft)
        
    def detect_Press(self) :
        self.state = False 

    def get_Length(self) :
        return self.image.get_width()

    def get_Left(self) :
        return self.rect.left

    def get_Right(self) :
        return self.rect.right