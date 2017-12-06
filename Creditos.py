#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame


from configuraciones import *
import MainJuego 



def Creditos(pantalla):

	pygame.init()
	pygame.display.flip()

	fin = False

	#TEXTOS
	title = "Creditos"
	l1 = "Realizacion: "
	l2 = "Juan Camilo Rojas Cortes, Johan Felipe Marin Gonzalez"
	l3 = "Universidad Tecnologica de Pereira"
	l4 = "Computacion Grafica"
	l5 = "Profesor: Carlos Andres Lopez"
	note = "Presione cualquier tecla para volver al Menu principal"

	#Fuentes
	fTitle = pygame.font.SysFont("monospace",40)
	fText = pygame.font.SysFont("monospace",30)
	fNote = pygame.font.SysFont("monospace",25)


	#Imágenes
	background = pygame.image.load('Imagenes/Menu/background.jpg')
	imgMario = pygame.image.load('Imagenes/Menu/marioTriste.jpg')
	imgTitle = fTitle.render(title,1,BLANCO)
	imgl1 = fText.render(l1,1,BLANCO)
	imgl2 = fText.render(l2,1,BLANCO)
	imgl3 = fText.render(l3,1,BLANCO)
	imgl4 = fText.render(l4,1,BLANCO)
	imgl5 = fText.render(l5,1,BLANCO)
	imgNote = fNote.render(note,1,ROJO)


	while not fin:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				fin = True
				return True

			if event.type == pygame.KEYDOWN:
				return False

		pantalla.fill(NEGRO)

		pantalla.blit(background,[0,-250])
		pantalla.blit(imgMario,[CENTRO[0] - 200,10])
		pantalla.blit(imgTitle,[CENTRO[0] - 150,250])
		pantalla.blit(imgl1,[0,300])
		pantalla.blit(imgl2,[0,350])
		pantalla.blit(imgl3,[50,400])
		pantalla.blit(imgl4,[50,450])
		pantalla.blit(imgl5,[50,500])
		pantalla.blit(imgNote,[0,550])

		pygame.display.flip()