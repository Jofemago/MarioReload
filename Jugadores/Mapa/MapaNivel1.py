
#EN este archivo se crea el elemento 1 de la sabanamapas
import pygame
from configuraciones import *

class base(pygame.sprite.Sprite):

    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(archivo).convert_alpha()
        self.image = archivo
        self.rect= self.image.get_rect()

    def setpos(self,x ,y):
        self.rect.x = x
        self.rect.y = y

    def getTipo(self):
        return 'nada'

    def update(self):
        pass


class suelo(base):

    def __init__(self, archivo):
        base.__init__(self,archivo)


class lava(pygame.sprite.Sprite):

    def __init__(self,x , y):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar('Jugadores/Mapa/imgmapas/lava.png',9,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.setPos(x,y)
        self.i = 0
        self.timesprite = 5
        self.actualizasprite = self.timesprite

    def getTipo(self):
        return 'lava'

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y


    def updateSprite(self):

        self.image = self.m[self.i][0]

    def movSprite(self):


        if self.actualizasprite < 0:
            if self.i < 7 :
                self.i += 1
            else:
                self.i = 0
            self.actualizasprite = self.timesprite
        self.actualizasprite -= 1



    def update(self):

        self.movSprite()
        self.updateSprite()


class bonus(pygame.sprite.Sprite):

    def __init__(self,x , y):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar('Jugadores/Mapa/imgmapas/bonus.png',4,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.setPos(x,y)
        self.i = 0
        self.timesprite = 10
        self.actualizasprite = self.timesprite

    def getTipo(self):
        return 'bonus'

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y


    def updateSprite(self):

        self.image = self.m[self.i][0]
    
    def movSprite(self):


        if self.actualizasprite < 0:
            if self.i < 2 :
                self.i += 1
            else:
                self.i = 0
            self.actualizasprite = self.timesprite
        self.actualizasprite -= 1



    def update(self):

        self.movSprite()
        self.updateSprite()
