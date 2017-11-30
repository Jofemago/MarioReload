import pygame
from configuraciones import *


class FireBall(pygame.sprite.Sprite):

    def __init__(self,imgSprite, dir = 0):
        pygame.sprite.Sprite.__init__(self)
        self.m = imgSprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.i = 0

        self.dy = 0
        self.dir = dir
        if self.dir == 1:
            self.dx = 10
        else:
            self.dx = -10


    def update(self):
        self.velocidades()
    	self.gravity()
        self.rebotar()
        self.movSprite()


    def movSprite(self):

        if self.i < 3:
    		self.i += 1
    	else:
    		self.i = 0
    	self.image = self.m[self.i][0]


    def velocidades(self):
        self.rect.x += self.dx
    	self.rect.y += self.dy

    def rebotar(self):
        if self.rect.y >= ALTO - self.rect.height:
            self.dy = -7

    def gravity(self):
    	self.dy += 0.45
