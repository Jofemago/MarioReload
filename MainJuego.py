import pygame

from configuraciones import *
from Nivel3 import *
from MainMenu import *
from Tutorial import *
from Creditos import *
from Historia import *

def main():
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO, ALTO])
	fin = False
	win = False
	while not fin and not win:
		option = Menu(pantalla)
		if option == 1:
			win = nivel3(pantalla)

		if option == 2:
			fin = Tutorial(pantalla)

		if option == 3:
			fin = Historia(pantalla)

		if option == 4:	
			fin = Creditos(pantalla)

		if option == 5:
			fin = True

if __name__ == '__main__':
	main()


