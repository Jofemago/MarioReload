import pygame

from configuraciones import *
from Nivel3 import *

if __name__ == '__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO, ALTO])
	win = nivel3(pantalla)

