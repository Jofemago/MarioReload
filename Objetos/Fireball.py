import pygame
from configuraciones import *


class FireBall(pygame.sprite.Sprite):

    def __init__(self,imgSprite):
        pygame.sprite.Sprite.__init__(self)
        self.m = imgSprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.i = 0
        self.dx = 10
        self.dy = 0


    def update(self):
    	self.rect.x += self.dx
    	self.rect.y += self.dy
    	self.gravity()
    	if self.i < 3:
    		self.i += 1
    	else:
    		self.i = 0
    	self.image = self.m[self.i][0]


    def rebotar(self):
    	self.dy = -10

    def gravity(self):
    	self.dy += 1