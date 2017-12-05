#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
        self.suelos = None
        self.vidas = 20
        self.dead = False
        self.caer = False #se activa cuando Peach está cayendo a la lava

    def update(self):

        self.validarColision()
        if self.rect.right >= ANCHO - 120 and not self.caer:
            self.left()

        if self.rect.left <= 0:
            self.right()


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

        self.rect.y += self.dy




        self.gravity()
        self.morir()


    def gravity(self):

        self.dy += 1

        


    def right(self):
        self.dir = 0
        self.dx = 10
        if self.dy == 0:
            self.jumping = False

    def left(self):
        self.dir = 1
        self.dx = -10
        if self.dy == 0:
            self.jumping = False

    def jump(self):
        if self.dy == 0:
            self.jumping = True
            self.dy = -15

    def beat(self,lado):
        self.jumping = False
        if lado == 0:
            self.dir = 2

        if lado == 1:
            self.dir = 3

    def keyup(self):
        if not self.jumping:
            self.dy = 0
        #if self.dy == 0:
            self.dx = 0


    def validarColision(self):

        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:# si de verdad hay colision
            for m in ls_bl:#otra solucion es que cuando toque por la parte de ariba del objeto la variacion en y sea 0

                if self.dx > 0 and not self.colArriba:
                    self.colIzquierda = True
                    self.rect.right = m.rect.left
                    self.col = True # haga colision true para que no afecte la gravedad
                    #self.gravedad()
                elif self.dx < 0 and not self.colArriba:
                    self.colDerecha = True
                    self.rect.left  = m.rect.right
                    self.col = True
                    #self.gravedad()
        else:
            self.col = False# si no hay colision active de nuevo la gravedad
            self.colDerecha = False
            self.colIzquierda = False

        self.rect.y += self.dy   #para que siempre juegue la gravedad
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:
            for m in ls_bl:
                if self.dy > 0 and self.rect.bottom >= m.rect.top:
                    self.colArriba = True
                    self.rect.bottom = m.rect.top
                    self.dy = 0
                    #como choca no puede estar en sprite de salto, esta montado en una platafoma
                    self.col = True


                elif self.dy < 0 and self.rect.top <= m.rect.bottom:
                    self.colAbajo = True
                    self.rect.top  = m.rect.bottom
                    self.dy = 0
                    self.col = True

                if self.rect.bottom > m.rect.top:
                    self.rect.bottom = m.rect.top


        else:
            self.col = False
            self.colArriba = False
            self.colAbajo = False


    def morir(self):
        if self.vidas == 0:
            self.dead = True
            self.vidas = -1
            self.caer = True
        else:
            self.dead = False


