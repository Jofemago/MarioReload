import pygame
from configuraciones import *









class Luigi(pygame.sprite.Sprite):

    def __init__(self,imgSprite):
        pygame.sprite.Sprite.__init__(self)
        self.m = imgSprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.dir = 0
        self.i = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        if self.dx != 0 or self.dy != 0:
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

        if self.dy >= 0:
            self.dy += 1.5

        if self.rect.bottom >= ALTO:
            self.dy = 0
            self.rect.bottom = ALTO



