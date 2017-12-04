#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

        self.suelos = pygame.sprite.Group()#se le pasan todos los suelos del mapa
        self.col = False #valida si en este momento hay una colisión
        self.colDerecha = False
        self.colArriba = False
        self.colAbajo = False
        self.colIzquierda = False

    def update(self):
        self.disparar()
        self.validarColision()
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


        if self.rect.right >= ANCHO and self.dx < 0 and not self.colDerecha and not self.colIzquierda:
            self.rect.x += self.dx

        if self.rect.left <= 0 and self.dx > 0 and not self.colDerecha and not self.colIzquierda:
            self.rect.x += self.dx

        if self.rect.top >= 0 and self.rect.bottom <= ALTO and self.dy > 0:
            self.rect.y += self.dy

        if self.rect.top >= 0 and self.rect.bottom <= ALTO:
            self.rect.y += self.dy

        if self.rect.top <= 0 and self.dy > 0:
            self.rect.y += self.dy





        self.gravity()


    def gravity(self):
        if not self.col:
            self.dy += 1

            if self.rect.bottom >= ALTO:
                self.dy = 0
                self.rect.bottom = ALTO

        else:
            self.dy == 0


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

    def validarColision(self):

        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:# si de verdad hay colision
            for m in ls_bl:#otra solucion es que cuando toque por la parte de ariba del objeto la variacion en y sea 0

                if self.rect.left == m.rect.right and self.dx > 0:
                    self.colIzquierda = True
                    self.rect.right = m.rect.left
                    self.col = True # haga colision true para que no afecte la gravedad
                    #self.gravedad()
                elif self.dx < 0 and self.rect.right == m.rect.left:
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
                if self.dy > 0 and self.rect.bottom == m.rect.top:
                    self.colArriba = True
                    self.rect.bottom = m.rect.top
                    #como choca no puede estar en sprite de salto, esta montado en una platafoma
                    self.col = True


                elif self.dy < 0 and m.rect.bottom == self.rect.top:
                    self.colAbajo = True
                    self.rect.top  = m.rect.bottom
                    self.dy = 0
                    self.col = True
        else:
            self.col = False
            self.colArriba = False
            self.colAbajo = False




