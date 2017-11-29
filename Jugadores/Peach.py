import pygame
from configuraciones import *







class Peach(pygame.sprite.Sprite):

    def __init__(self,imgSprite):
        pygame.sprite.Sprite.__init__(self)
        self.m = imgSprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.dir = 0
        self.i = 0
        self.dx = 0
        self.dy = 0
        self.jumping = False

    def update(self):
        if self.dx != 0 or self.dy != 0 or self.dir == 2 or self.dir == 3:
            if self.i < 3:
                self.i += 1
            else:
                self.i = 0
        self.image = self.m[self.i][self.dir]
        if self.rect.right <= ANCHO and self.rect.left >= 0:
            self.rect.x += self.dx

        if self.rect.right >= ANCHO and self.dx < 0:
            self.rect.x += self.dx

        if self.rect.left <= 0 and self.dx > 0:
            self.rect.x += self.dx

        if self.rect.top >= 0 and self.rect.bottom <= ALTO:
            self.rect.y += self.dy

        if self.rect.top <= 0 and self.dy > 0:
            self.rect.y += self.dy

        if self.rect.bottom >= ALTO and self.dy < 0:
            self.rect.y += self.dy




        self.gravity()


    def gravity(self):

        self.dy += 1

        if self.rect.bottom >= ALTO:
            self.dy = 0
            self.rect.bottom = ALTO


    def right(self):
        self.dir = 0
        self.dx = 5
        if self.dy == 0:
            self.jumping = False

    def left(self):
        self.dir = 1
        self.dx = -5
        if self.dy == 0:
            self.jumping = False

    def jump(self):
        if self.dy == 0:
            self.jumping = True
            self.dy = -15

    def beat(self):
        self.jumping = False
        if self.dir == 0:
            self.dir = 2

        if self.dir == 1:
            self.dir = 3

    def keyup(self):
        if not self.jumping:
            self.dy = 0
        #if self.dy == 0:
            self.dx = 0


