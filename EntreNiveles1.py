import pygame

from configuraciones import *


def EntreNiveles1(pantalla,bonus,nivel):
	pygame.init()
	pygame.display.flip()

	fin = False

	background = pygame.image.load('Imagenes/Menu/background.jpg')

	title = "FELICIDADES"
	t1 = "Ganaste el nivel " + str(nivel)
	t2 = "Bonus: " + str(bonus)
	t3 = "Presiona una tecla para continuar"

	fTitle = pygame.font.SysFont("monospace",40)
	fT = pygame.font.SysFont("monospace",30)

	imgTitle = fTitle.render(title,1,BLANCO)
	imgT1 = fT.render(t1,1,BLANCO)
	imgT2 = fT.render(t2,1,BLANCO)
	imgT3 = fT.render(t3,1,BLANCO)

	while not fin:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				fin = True
				return True

			if event.type == pygame.KEYDOWN:
				return False


		pantalla.blit(background,[0,-250])
		pantalla.blit(imgTitle,[CENTRO[0] - 200,10])
		pantalla.blit(imgT1,[CENTRO[0] - 200,100])
		pantalla.blit(imgT2,[CENTRO[0] - 200,200])
		pantalla.blit(imgT3,[CENTRO[0] - 200,300])
		pygame.display.flip()