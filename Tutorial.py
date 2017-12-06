#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from configuraciones import *
from MainJuego import *


def Tutorial(pantalla):
	pygame.init()
	pygame.display.flip()
	clock = pygame.time.Clock()

	fin = False

	#TEXTOS:
	title = "MARIO RELOAD"
	title2 = "Tutorial"
	mover = "Mover: "
	disparar = "Disparar: "
	note = "Presiona una tecla para volver al menu principal"

	#Fuentes:
	fTitle = pygame.font.SysFont("monospace",40)
	fTitle2 = pygame.font.SysFont("monospace",35)
	fText = pygame.font.SysFont("monospace",35)
	fNote = pygame.font.SysFont("monospace",20)


	#IMÁGENES INICIALES:
	background = pygame.image.load('Imagenes/Menu/background.jpg')
	imgMario = pygame.image.load('Imagenes/Menu/marioTriste.jpg')
	flechas = pygame.image.load('Imagenes/Tutorial/Flechas.jpg')
	espacio = pygame.image.load('Imagenes/Tutorial/Espacio.jpg')
	imgTitle = fTitle.render(title,1,BLANCO)
	imgTitle2 = fTitle2.render(title2,1,BLANCO)
	imgMover = fText.render(mover,1,BLANCO)
	imgDisparar = fText.render(disparar,1,BLANCO)
	imgNote = fNote.render(note,1,BLANCO)



	while not fin:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				return False

		pantalla.fill(NEGRO)
		pantalla.blit(background,[0,-250])
		pantalla.blit(imgMario,[CENTRO[0] - 200,10])
		pantalla.blit(imgTitle,[CENTRO[0] - 150,250])
		pantalla.blit(imgTitle2,[CENTRO[0] - 130,290])
		pantalla.blit(imgMover,[CENTRO[0]-200,330])
		pantalla.blit(flechas,[ANCHO - 400,330])
		pantalla.blit(imgDisparar,[CENTRO[0] - 200,440])
		pantalla.blit(espacio,[ANCHO - 400,440])
		pantalla.blit(imgNote,[100, ALTO - 100])
		
		pygame.display.flip()

