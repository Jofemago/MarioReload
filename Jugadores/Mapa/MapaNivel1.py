
#EN este archivo se crea el elemento 1 de la sabanamapas
import pygame
from configuraciones import *

class suelo(pygame.sprite.Sprite):

    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(archivo).convert_alpha()
        self.image = archivo
        self.rect= self.image.get_rect()

    def setpos(self,x ,y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass
