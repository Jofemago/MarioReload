#EN este archivo se crea el elemento 1 de la sabanamapas
import pygame
from configuraciones import *


class Goomba(pygame.sprite.Sprite):

    def __init__(self,x,y, archivo,suelos):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar(archivo,3,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.bonus = 500 #cantidad de puntos que entrega esta hazana

        self.setPos(x,y + 4)
        #validar si el mrio lo ha golpeado
        self.golpe = False
        self.tiempoDestruccion = 10
        self.tipo = False

        self.i = 0
        self.suelos = suelos
        self.var_basesprite = 5 # cada cuanto se activa el sprite
        self.var_sprite = self.var_basesprite

        #movimiento en el mapa
        self.dir = 2 #va de izquierda a derecha inicialmente
        self.var_x = 3
        self.var_y = 0
        self.col = False

    def gravedad(self):

        #si no hya colision que empiece a bajar haciendo efecto de gravedad
        if not self.col:
            if self.var_y == 0:
                self.var_y = 1
            else:
                self.var_y += 1


    def validarColision(self):
        self.rect.x += self.var_x
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:# si de verdad hay colision
            for m in ls_bl:#otra solucion es que cuando toque por la parte de ariba del objeto la variacion en y sea 0

                if self.var_x > 0:
                    self.rect.right = m.rect.left
                    self.dir = 1
                    self.col = True # haga colision true para que no afecte la gravedad
                    #self.gravedad()
                elif self.var_x < 0:
                    self.rect.left  = m.rect.right
                    self.dir  = 2
                    self.col = True

                    #self.rect.x += self.var_x
                    #self.gravedad()
        else:
            self.col = False# si no hay colision active de nuevo la gravedad

        self.rect.y += self.var_y   #para que siempre juegue la gravedad
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:
            for m in ls_bl:
                if self.var_y > 0:
                    self.rect.bottom = m.rect.top -4
                    #como choca no puede estar en sprite de salto, esta montado en una platafoma
                    #self.saltar = False
                    self.col = True



                elif self.var_y < 0:
                    self.rect.top  = m.rect.bottom


                    self.var_y = 0
                    self.col = True
        else:
            self.col = False


    def MoverSprite(self):

        if self.var_sprite <= 0:

            if self.i < 1 :
                self.i += 1
            else:
                self.i = 0
                #self.rect.x += 100
            self.var_sprite = self.var_basesprite
        self.var_sprite -= 1

    def ubicarimg(self):
        self.image = self.m[self.i][0]


    def movimientoX(self):
        #print self.dir
        if self.dir == 2:
            self.var_x = 3
        else:
            self.var_x = -3

    def setPos(self,x,y):

        self.rect.x = x
        self.rect.y = y

    def destruir(self):

        if self.rect.y >= ANCHO:
            self.kill()

    def update(self):
        if self.rect.x >= -100 and self.rect.x < ANCHO:
            if not self.golpe:
                self.MoverSprite()
                self.ubicarimg()

                self.gravedad()
                self.movimientoX()
                self.validarColision()
                self.destruir()
            else:
                self.image = self.m[2][0]
                if self.tiempoDestruccion <= 0:
                    self.kill()
                self.tiempoDestruccion -= 1
        else:
            self.dir = 1



class Carnivora(pygame.sprite.Sprite):

    def __init__(self,x,y, archivo):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar(archivo,7,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.bonus = 1000 #cantidad de puntos que entrega esta hazana

        self.setPos(x+20,y-10)
        #validar si el mrio lo ha golpeado

        self.i = 0
        self.tiempoCero = False
        self.tiempoBase = 100
        self.tiempo = self.tiempoBase

        self.var_basesprite = 10 # cada cuanto se activa el sprite
        self.var_sprite = self.var_basesprite


    def MoverSprite(self):

        if self.var_sprite <= 0:

            if self.i < 6 :
                self.i += 1
            else:
                self.i = 0
                self.tiempoCero = True
                #self.rect.x += 100
            self.var_sprite = self.var_basesprite
        self.var_sprite -= 1

    def ubicarimg(self):
        self.image = self.m[self.i][0]



    def setPos(self,x,y):

        self.rect.x = x
        self.rect.y = y

    def destruir(self):

        if self.rect.y >= ANCHO:
            self.kill()
        if self.rect.x <= -70:
            self.kill()

    def update(self):
        if self.rect.x >= -100 and self.rect.x < ANCHO:

            if not self.tiempoCero:
                self.MoverSprite()
                self.tiempo = self.tiempoBase
            else:
                if self.tiempo <= 0:
                    self.tiempoCero = False
                self.tiempo -= 1

            self.ubicarimg()

        else:
            self.dir = 1
