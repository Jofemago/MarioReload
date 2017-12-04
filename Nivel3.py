#!/usr/bin/env python
# -*- coding: utf-8 -*-



import pygame
import random

from configuraciones import *
from Jugadores.Luigi import *
from Jugadores.Mario import *
from Jugadores.Peach import *
from Objetos.Fireball import *
from Jugadores.Mapa.ControllerMapa import *


def nivel3(pantalla):
	pygame.init()

	#se llaman las sábanas de sprites
	imgmariopeque = 'Jugadores/imgJugador/pequemario.png'
	imgmariogrande = 'Jugadores/imgJugador/mariogrande.png'
	imgmariofuego = 'Jugadores/imgJugador/MarioFuego.png'
	imgbolafuego = 'Objetos/boladefuego.png'
	imgLuigi = 'Jugadores/imgJugador/luigi.png'
	imgPeach = 'Jugadores/imgJugador/peach.png'
	sabanamapas = 'Jugadores/Mapa/imgmapas/sabanamapas.png'

	mapa = ConfiguracionJson('Jugadores/Mapa/jsonmapas/nivel3.json')

	#se definen las matrices de imágenes para todos los sprites
	corteMario1 = recortar(imgmariopeque,3,5)
	corteMario2 = recortar(imgmariogrande,3,5)
	corteMario3 = recortar(imgmariofuego,3,5)
	corteLuigi = recortar(imgLuigi,4,4)
	cortePeach = recortar(imgPeach,4,4)
	corteBola = recortar(imgbolafuego,4,1)

	#definición de personajes
	mario = Mario(corteMario1,corteMario2,corteMario3)
	luigi = Luigi(corteLuigi)
	peach = Peach(cortePeach)

	#definición de grupos
	gMario = pygame.sprite.Group()
	gLuigi = pygame.sprite.Group()
	gPeach = pygame.sprite.Group()
	bolasMario = pygame.sprite.Group()
	bolasLuigi = pygame.sprite.Group()
	general = pygame.sprite.Group()


	#configuración inicial de personajes
	mario.rect.bottom = ALTO
	mario.rect.x = 10
	mario.estado = 3
	luigi.rect.bottom = ALTO
	luigi.rect.x = ANCHO - 120
	peach.rect.bottom = ALTO
	peach.rect.x = ANCHO - 50

	#agregar personajes a los grupos
	gMario.add(mario)
	gLuigi.add(luigi)
	gPeach.add(peach)
	#general.add(mario)
	#general.add(luigi)
	general.add(peach)

	#Grupos de elementos del mapa
	suelos = pygame.sprite.Group()
	fondos = pygame.sprite.Group()

	controllerMapa = MakeMapa(mapa,recortar(sabanamapas,10,10),suelos,fondos,general)
	controllerMapa.dibujarmapa()

	#se añaden los grupos de suelos a los personajes
	mario.suelos = suelos
	luigi.suelos = suelos








	pygame.display.flip()
	clock = pygame.time.Clock()

	fin = False

	levantarLuigi = 40 #variable que se utilizará para simular que Luigi levanta la tecla y deja de hacer algo

	while not fin:

		rand = random.randrange(1,6)#variable aleatoria que decidirá la acción de Luigi
		levantarLuigi -= 1


		if levantarLuigi == 0:#debe hacer algo
			if rand == 1:
				luigi.right()
			if rand == 2:
				luigi.left()
			if rand == 3:
				luigi.jump()
			if rand == 4:
				luigi.jump()
				luigi.right()
			if rand == 5:
				luigi.jump()
				luigi.left()
			if rand == 6:
				luigi.keyup()

			levantarLuigi = 30

			#si se choca con un muro, se devuelve. Posteriormente, se deberá reemplazar con la colisión con un muro del mapa

		if luigi.rect.left <= 0:
			luigi.right()
		if luigi.rect.right >= ANCHO:
			luigi.left()

			

		if luigi.disparo:
			bola = FireBall(corteBola,suelos)
			if luigi.dir == 0:
				bola.dir = 1
			if luigi.dir == 1:
				bola.dir = 0
			bola.rect.center = luigi.rect.center
			bolasLuigi.add(bola)
			general.add(bola)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_RIGHT:
					mario.dir = 1
					mario.var_x = 5
					mario.var_basesprite = mario.sprite

				if event.key == pygame.K_LEFT:
					mario.dir = 0
					mario.var_x = -5
					mario.var_basesprite = mario.sprite

				if event.key == pygame.K_SPACE:
					if mario.estado == 3 and not mario.disparo:
						bola = FireBall(corteBola,suelos,mario.dir)
						bola.rect.center = mario.rect.center
						general.add(bola)
						bolasMario.add(bola)
						mario.disparo = True


				if event.key == pygame.K_UP:
					mario.salto()


			if event.type == pygame.KEYUP:

				if event.key == pygame.K_RIGHT and mario.var_x > 0:
					mario.var_x = 0

				if event.key == pygame.K_LEFT and mario.var_x < 0:
					mario.var_x = 0





		pantalla.fill(NEGRO)
		general.update()
		gMario.update()
		gLuigi.update()
		general.draw(pantalla)
		gMario.draw(pantalla)
		gLuigi.draw(pantalla)
		bolasMario.draw(pantalla)
		bolasLuigi.draw(pantalla)
		pygame.display.flip()
		clock.tick(30)


