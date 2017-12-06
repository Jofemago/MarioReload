import pygame

from configuraciones import *
from Nivel3 import *
from MainMenu import *
from Tutorial import *
from Creditos import *
from Historia import *
from Nivel1 import *
from Nivel2 import *
from EntreNiveles1 import *

def main():
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO, ALTO])
	fin = False
	win = False
	while not fin and not win:
		option = Menu(pantalla)
		if option == 1:
			elementos = Nivel1(pantalla)
			if elementos[0] == True:
				fin = EntreNiveles1(pantalla,elementos[2],1)
				if not fin:
					elementos2 = Nivel2(pantalla,elementos[1],elementos[2])
					if elementos2[0] == True:
						fin = EntreNiveles1(pantalla,elementos2[2],2)
						if not fin:
							nivel3(pantalla)

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


