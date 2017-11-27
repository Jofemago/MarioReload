
import pygame
from configuraciones import *

class Mario(pygame.sprite.Sprite):

    def __init__(self,imgpeque, col = AZUL):

        pygame.sprite.Sprite.__init__(self)
        self.m = imgpeque
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.setPos(100,0)


        #variables para los movimientos de sprites
        self.dir = 0
        self.i = 0

        #variables de movimiento
        self.var_x =  0
        self.var_y = 0
        #self.vidas = vidas
        self.plataformas =  pygame.sprite.Group()
        self.col = False

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y

    def setX(self, x):

        self.rect.x = x

    def setX(self, y):

        self.rect.x = y

    def movX(self):

        if self.rect.x >= ANCHO -50 and self.var_x >= 0:
            self.var_x = 0

        if self.rect.x <= 0 and self.var_x <= 0:
            self.var_x = 0


        self.rect.x += self.var_x

    def movY(self):


        if self.rect.y >= ALTO - 60 and self.var_y >= 0:
            self.var_y = 0

        if self.rect.y <= 100 and self.var_y <= 0:
            self.var_y = 0




        self.rect.y += self.var_y


    def gravedad(self):

        #si no hya colision que empiece a bajar haciendo efecto de gravedad
        if not self.col:
            if self.var_y == 0:
                self.var_y = 1
            else:
                self.var_y += 0.25

        #bordes
        if self.rect.y >= ALTO - self.rect.height  and self.var_y >= 0:
            self.var_y = 0
            self.rect.y = ALTO - self.rect.height

    def salto(self):
        self.var_y = -10 #haga la variable de salto y mueva elsprite hasta la posicion indicada
        #este mientras sube ira perdiendo la altura con la gravedad activa

    def gritar(self):
        #self.sonido.play()
        pass

    def validarColision(self):

        ls_bl = pygame.sprite.spritecollide(self,self.plataformas, False)
        if len(ls_bl) > 0:# si de verdad hay colision
            for m in ls_bl:#otra solucion es que cuando toque por la parte de ariba del objeto la variacion en y sea 0

                if self.var_x > 0:
                    self.rect.right = m.rect.left
                    self.col = True # haga colision true para que no afecte la gravedad
                    #self.gravedad()
                elif self.var_x < 0:
                    self.rect.left  = m.rect.right
                    self.col = True
                    #self.gravedad()
        else:
            self.col = False# si no hay colision active de nuevo la gravedad

        self.rect.y += self.var_y
        ls_bl = pygame.sprite.spritecollide(self,self.plataformas, False)
        if len(ls_bl) > 0:
            for m in ls_bl:
                if self.var_y > 0:
                    self.rect.bottom = m.rect.top
                    self.col = True


                elif self.var_y < 0:
                    self.rect.top  = m.rect.bottom
                    self.var_y = 0
                    self.col = True
        else:
            self.col = False


    def movSprite(self):

        if self.var_y != 0 or self.var_x != 0:
            if self.i < 2 :

                self.i += 1
            else:
                self.i = 0
        self.image = self.m[self.i][self.dir]
        #self.rect = self.image.get_rect()
        self.rect.x += self.var_x


    def update(self):

        self.movX()
        #self.rect.y += self.var_y

        self.gravedad()
        #colisiones
        self.validarColision()

        #movimiento de los sprites
        self.movSprite()
