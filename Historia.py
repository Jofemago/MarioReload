#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from configuraciones import *


def Historia(pantalla):
	pygame.init()
	pygame.display.flip()
	fin = False

	#TEXTO
	title = "MARIO RELOAD"
	l1 = "Mario es un fontanero enamorado de su princesa: Peach."
	l2 = "Lastimosamente, Peach se encuentra secuestrada, por lo que Mario"
	l3 = "se dispone a arriesgar su vida por su amada."
	l4 = "Es necesario atravesar campos con muchos peligros para sobrevivir y llegar a Peach."
	l5 = "Sin embargo, a medida que va avanzando, Mario va destapando poco a poco"
	l6 = "una desagradable sorpresa, ayudado por su amigo Lakitu."
	l7 = "Para descubrir del todo la historia oculta de Peach, Mario tiene que llegar hasta el final."
	l8 = "¿Puedes ayudarlo?"

	nota = "Presiona una tecla para volver al menu"


	#FUENTES
	fTitle = pygame.font.SysFont("monospace",40)
	fText = pygame.font.SysFont("monospace",15)
	fNota = pygame.font.SysFont("monospace",25)

	#IMÁGENES
	background = pygame.image.load('Imagenes/Menu/background.jpg')
	imgMario = pygame.image.load('Imagenes/Menu/marioTriste.jpg')
	imgTitle = fTitle.render(title,1,BLANCO)
	imgl1 = fText.render(l1,1,BLANCO)
	imgl2 = fText.render(l2,1,BLANCO)
	imgl3 = fText.render(l3,1,BLANCO)
	imgl4 = fText.render(l4,1,BLANCO)
	imgl5 = fText.render(l5,1,BLANCO)
	imgl6 = fText.render(l6,1,BLANCO)
	imgl7 = fText.render(l7,1,BLANCO)
	imgl8 = fText.render(l8,1,BLANCO)
	imgNota = fNota.render(nota,1,BLANCO)

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
		pantalla.blit(imgl2,[0,320])
		pantalla.blit(imgl3,[0,340])
		pantalla.blit(imgl4,[0,360])
		pantalla.blit(imgl5,[0,380])
		pantalla.blit(imgl6,[0,400])
		pantalla.blit(imgl7,[0,420])
		pantalla.blit(imgl8,[0,440])
		pantalla.blit(imgNota,[50,500])

		pygame.display.flip()