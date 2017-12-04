import pygame
from configuraciones import *


class FireBall(pygame.sprite.Sprite):

    def __init__(self,imgSprite,suelos, dir = 0):
        pygame.sprite.Sprite.__init__(self)
        self.m = imgSprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.i = 0

        #sprite de muros que srve para que la vala choque
        self.suelos = suelos


        self.dy = 0
        self.dir = dir
        if self.dir == 1:
            self.dx = 8
        else:
            self.dx = -8


    def update(self):
        self.velocidades()
    	self.gravity()
        #self.validarColision()
        #self.rebotar()
        self.movSprite()
        self.validarLimites()





    def movSprite(self):

        if self.i < 3:
    		self.i += 1
    	else:
    		self.i = 0
    	self.image = self.m[self.i][0]


    def velocidades(self):

        self.rect.x += self.dx
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:# si de verdad hay colision
            for m in ls_bl:#otra solucion es que cuando toque por la parte de ariba del objeto la variacion en y sea 0

                self.kill()
                """if self.dir == 0:
                    self.rect.right = m.rect.left

                    #self.gravedad()
                elif self.dir == 1 :
                    self.rect.left  = m.rect.right
                    self.col = True"""

    	self.rect.y += self.dy
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:
            for m in ls_bl:
                #pass
                if  self.rect.y >= m.rect.y - 15:
                    self.rect.bottom = m.rect.top
                    self.Rebotar()
                    #como choca no puede estar en sprite de salto, esta montado en una platafoma


                    """
                elif self.var_y < 0:
                    self.rect.top  = m.rect.bottom"""




    def validarLimites(self):

        if self.rect.x > ANCHO:
            self.kill()
        if self.rect.x < 0 - self.rect.width:
            self.kill()

        if self.rect.y > ALTO:
            self.kill()


    def Rebotar(self):
        self.dy = -7

    def rebotar(self):
        if self.rect.y >= ALTO - self.rect.height:
            self.dy = -7

    def gravity(self):
    	self.dy += 0.45
