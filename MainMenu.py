#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame

from configuraciones import *


def Menu(pantalla):
	pygame.init()
	pygame.display.flip()
	clock = pygame.time.Clock()

	fin = False

	#CARGA DE IMÁGENES
	background = pygame.image.load('Imagenes/Menu/background.jpg')
	imgMario = pygame.image.load('Imagenes/Menu/marioTriste.jpg')

	#TEXTOS MENÚ:
	title = "MARIO RELOAD"
	h = "Selecciona:"
	op1 = "Iniciar juego"
	op2 = "Tutorial"
	op3 = "Historia"
	op4 = "Creditos"
	op5 = "Salir"

	#FUENTES:
	fTitle = pygame.font.SysFont("monospace",40)
	fH = pygame.font.SysFont("monospace",35)
	fop = pygame.font.SysFont("monospace",30)

	#IMÁGENES:
	imgTitle = fTitle.render(title,1,BLANCO)
	imgH = fH.render(h,1,BLANCO)

	select = 1 #se utiliza para la opción seleccionada



	while not fin:

		if select == 1:
			imgOP1 = fop.render(op1,1,ROJO)
			imgOP2 = fop.render(op2,1,BLANCO)
			imgOP3 = fop.render(op3,1,BLANCO)
			imgOP4 = fop.render(op4,1,BLANCO)
			imgOP5 = fop.render(op5,1,BLANCO)

		if select == 2:
			imgOP1 = fop.render(op1,1,BLANCO)
			imgOP2 = fop.render(op2,1,ROJO)
			imgOP3 = fop.render(op3,1,BLANCO)
			imgOP4 = fop.render(op4,1,BLANCO)
			imgOP5 = fop.render(op5,1,BLANCO)

		if select == 3:
			imgOP1 = fop.render(op1,1,BLANCO)
			imgOP2 = fop.render(op2,1,BLANCO)
			imgOP3 = fop.render(op3,1,ROJO)
			imgOP4 = fop.render(op4,1,BLANCO)
			imgOP5 = fop.render(op5,1,BLANCO)

		if select == 4:
			imgOP1 = fop.render(op1,1,BLANCO)
			imgOP2 = fop.render(op2,1,BLANCO)
			imgOP3 = fop.render(op3,1,BLANCO)
			imgOP4 = fop.render(op4,1,ROJO)
			imgOP5 = fop.render(op5,1,BLANCO)

		if select == 5:
			imgOP1 = fop.render(op1,1,BLANCO)
			imgOP2 = fop.render(op2,1,BLANCO)
			imgOP3 = fop.render(op3,1,BLANCO)
			imgOP4 = fop.render(op4,1,BLANCO)
			imgOP5 = fop.render(op5,1,ROJO)


	
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				fin = True
				return 5 #para que salga

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:
					if select == 1:
						select = 5
					else:
						select -= 1

				if event.key == pygame.K_DOWN:
					if select == 5:
						select = 1
					else:
						select += 1


				if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
					return select


		pantalla.fill(NEGRO)
		pantalla.blit(background,[0,-250])
		pantalla.blit(imgTitle,[CENTRO[0] - 150,250])
		pantalla.blit(imgH,[CENTRO[0] - 130,290])
		pantalla.blit(imgMario,[CENTRO[0] - 200,10])
		pantalla.blit(imgOP1,[CENTRO[0]-200,330])
		pantalla.blit(imgOP2,[CENTRO[0]-200,360])
		pantalla.blit(imgOP3,[CENTRO[0]-200,390])
		pantalla.blit(imgOP4,[CENTRO[0]-200,420])
		pantalla.blit(imgOP5,[CENTRO[0]-200,450])
		pygame.display.flip()

