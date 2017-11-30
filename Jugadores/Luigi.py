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
        self.contSprite = 0
        self.jumping = False
        self.tiempoDisparo = 40 # define que Luigi dispare cada determinado tiempo
        self.disparo = False #valida que se dispare en el momento

    def update(self):
        self.disparar()
        if self.dx != 0 or self.dy != 0:
            self.contSprite += 1

            if self.contSprite == 3:
                self.contSprite = 0

            if self.i < 3 and self.contSprite == 0:
                self.i += 1
            elif self.i == 3:
                self.i = 0


        self.image = self.m[self.i][self.dir]
        if self.rect.right <= ANCHO and self.rect.left >= 0:
            self.rect.x += self.dx


        if self.rect.right >= ANCHO and self.dx < 0:
            self.rect.x += self.dx

        if self.rect.left <= 0 and self.dx > 0:
            self.rect.x += self.dx

        if self.rect.top >= 0 and self.rect.bottom <= ALTO and self.dy > 0:
            self.rect.y += self.dy

        if self.rect.top >= 0 and self.rect.bottom <= ALTO:
            self.rect.y += self.dy

        if self.rect.top <= 0 and self.dy > 0:
            self.rect.y += self.dy





        self.gravity()


    def gravity(self):

        self.dy += 1

        if self.rect.bottom >= ALTO:
            self.dy = 0
            self.rect.bottom = ALTO


    def left(self):
        self.dir = 1
        self.dx = -8
        if self.dy == 0:
            self.jumping = False

    def right(self):
        self.dir = 0
        self.dx = 8
        if self.dy == 0:
            self.jumping = False

    def jump(self):
        self.jumping = True
        if self.dir == 0:
            self.dir = 2
        if self.dir == 1:
            self.dir = 3
        if self.dy == 0:
            self.dy = -20

    def keyup(self):
        if not self.jumping:
            self.dx = 0
            self.dy = 0


    def disparar(self):
        self.tiempoDisparo -= 1
        if not self.disparo:
            if self.tiempoDisparo == 0:
                self.disparo = True

        if self.tiempoDisparo == 0:
            self.tiempoDisparo = 40
        else:
            self.disparo = False




