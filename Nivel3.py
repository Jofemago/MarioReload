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


def movePeach(peach):
	rand = random.randrange(1,6)
	if rand == 1 and peach.rect.right < ANCHO - 150:
		peach.right()
	if rand == 2:
		peach.left()
	if rand == 3:
		peach.jump()
	if rand == 4:
		peach.jump()
		peach.right()
	if rand == 5:
		peach.jump()
		peach.left()
	if rand == 6:
		peach.keyup()



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
	corteMario1 = recortar(imgmariopeque,4,5)
	corteMario2 = recortar(imgmariogrande,4,5)
	corteMario3 = recortar(imgmariofuego,4,5)
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
	mario.rect.bottom = ALTO - 40
	mario.rect.x = 10
	mario.estado = 3
	mario.image = mario.m[0][1]
	luigi.rect.center = [ANCHO - 240, ALTO - 160]#para que aparezca montado en la plataforma
	peach.rect.bottom = ALTO - 40
	peach.rect.right = ANCHO - 110 #para que aparezca escondida detrás de la plataforma

	#agregar personajes a los grupos
	gMario.add(mario)
	gLuigi.add(luigi)
	gPeach.add(peach)
	#general.add(mario)
	#general.add(luigi)
	#general.add(peach)

	#Grupos de elementos del mapa
	suelos = pygame.sprite.Group()
	fondos = pygame.sprite.Group()
	cuadros = pygame.sprite.Group()
	Bonus = pygame.sprite.Group()

	controllerMapa = MakeMapa(mapa,recortar(sabanamapas,10,10),suelos,fondos,general,cuadros,Bonus)
	controllerMapa.dibujarmapa()

	controllerMapa.dibujarFondo(3)

	#se añaden los grupos de suelos a los personajes
	mario.suelos = suelos
	luigi.suelos = suelos
	peach.suelos = suelos


	peleaPeach = False  #se activará cuando a Mario le toque pelear con Peach


	vidasMario = 20

	marioDead = False #controla si Mario está muerto




	#VARIABLES PARA CONTROLAR LOS DIÁLOGOS
	#DIÁLOGO INICIAL
	#Rutas de las imagenes:
	imgD1 = 'Imagenes/Dialogos/tercerNivel/Inicial/1.png'
	imgD2 = 'Imagenes/Dialogos/tercerNivel/Inicial/2.png'
	imgD3 = 'Imagenes/Dialogos/tercerNivel/Inicial/3.png'
	imgD4 = 'Imagenes/Dialogos/tercerNivel/Inicial/4.png'
	imgD5 = 'Imagenes/Dialogos/tercerNivel/Inicial/5.png'
	imgD6 = 'Imagenes/Dialogos/tercerNivel/Inicial/6.png'

	#Carga de imágenes:
	D1 = pygame.image.load(imgD1)
	D2 = pygame.image.load(imgD2)
	D3 = pygame.image.load(imgD3)
	D4 = pygame.image.load(imgD4)
	D5 = pygame.image.load(imgD5)
	D6 = pygame.image.load(imgD6)

	tDialogo = 0 #se usará para controlar el tiempo de aparición de cada diálogo

	#Banderas para aparición de diálogos:
	BD1 = False
	BD2 = False
	BD3 = False
	BD4 = False
	BD5 = False
	BD6 = False


	#DIÁLOGO FINAL
	imgDF1 = 'Imagenes/Dialogos/tercerNivel/Final/F1.png'
	imgDF2 = 'Imagenes/Dialogos/tercerNivel/Final/F2.png'
	imgDF3 = 'Imagenes/Dialogos/tercerNivel/Final/F3.png'
	imgDF4 = 'Imagenes/Dialogos/tercerNivel/Final/F4.png'

	#Carga de imágenes:
	DF1 = pygame.image.load(imgDF1)
	DF2 = pygame.image.load(imgDF2)
	DF3 = pygame.image.load(imgDF3)
	DF4 = pygame.image.load(imgDF4)

	#Banderas para la aparición de diálogos
	BDF1 = False
	BDF2 = False
	BDF3 = False
	BDF4 = False

	tDialogoF = 0 #variable para los tiempos del diálogo final


	#DIÁLOGO CUANDO MARIO GANA:
	imgDF5 = 'Imagenes/Dialogos/tercerNivel/Final/F5.png'
	imgDF6 = 'Imagenes/Dialogos/tercerNivel/Final/F6.png'
	DF5 = pygame.image.load(imgDF5)
	DF6 = pygame.image.load(imgDF6)

	tDialogoFF = 0 #variable para los tiempos del diálogo cuando Mario gana

	BDF5 = False
	BDF6 = False




	#Imagen de Lakitu
	rLakitu = 'Imagenes/Latiku/Latiku.png'
	Lakitu = pygame.image.load(rLakitu)



	pygame.display.flip()
	clock = pygame.time.Clock()

	fin = False

	levantarLuigi = 40 #variable que se utilizará para simular que Luigi levanta la tecla y deja de hacer algo
	puntosPeach = 4 #cuando está golpeando, cada cuatro ciclos se quita un punto

	win = False #Al final es la variable que se va a retornar


	while not fin:

		#control de diálogos
		if tDialogo >= 0 and tDialogo < 90:
			BD1 = True
			BD2 = False
			BD3 = False
			BD4 = False
			BD5 = False
			BD6 = False

		if tDialogo >= 90 and tDialogo < 180:
			BD1 = False
			BD2 = True
			BD3 = False
			BD4 = False
			BD5 = False
			BD6 = False

		if tDialogo >= 180 and tDialogo < 270:
			BD1 = False
			BD2 = False
			BD3 = True
			BD4 = False
			BD5 = False
			BD6 = False

		if tDialogo >= 270 and tDialogo < 360:
			BD1 = False
			BD2 = False
			BD3 = False
			BD4 = True
			BD5 = False
			BD6 = False

		if tDialogo >= 360 and tDialogo < 450:
			BD1 = False
			BD2 = False
			BD3 = False
			BD4 = False
			BD5 = True
			BD6 = False

		if tDialogo >= 450 and tDialogo < 540:
			BD1 = False
			BD2 = False
			BD3 = False
			BD4 = False
			BD5 = False
			BD6 = True

		if tDialogo >= 630:
			BD1 = False
			BD2 = False
			BD3 = False
			BD4 = False
			BD5 = False
			BD6 = False

		tDialogo += 1


		#CONTROL DE DIÁLOGOS FINALES:
		if luigi.caer:
			if tDialogoF >= 0 and tDialogoF < 90:
				BDF1 = True
				BDF2 = False
				BDF3 = False
				BDF4 = False

			if tDialogoF >= 90 and tDialogoF < 180:
				BDF1 = False
				BDF2 = True
				BDF3 = False
				BDF4 = False

			if tDialogoF >= 180 and tDialogoF < 270:
				BDF1 = False
				BDF2 = False
				BDF3 = True
				BDF4 = False

			if tDialogoF >= 270 and tDialogoF < 360:
				BDF1 = False
				BDF2 = False
				BDF3 = False
				BDF4 = True

			if tDialogoF >= 360:
				BDF1 = False
				BDF2 = False
				BDF3 = False
				BDF4 = False

			tDialogoF += 1


		rand = random.randrange(1,6)#variable aleatoria que decidirá la acción de Luigi
		levantarLuigi -= 1
		if levantarLuigi == 0 and peleaPeach and not peach.caer:
			movePeach(peach)
			levantarLuigi = 30

		if levantarLuigi == 0 and not luigi.caer:#debe hacer algo
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

		if luigi.rect.left <= 0 and not luigi.dead:
			luigi.right()
		if luigi.rect.right >= ANCHO and not luigi.dead:
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

		if luigi.dead:
			luigi.dx = 0
			luigi.rect.top = 100
			luigi.rect.right = ANCHO - 80

			luigi.gravity()
			luigi.vida = -1
			#pausa1 = True # para que se muestre el mensaje de que Luigi murió
			luigi.dead = False#para que no vuelva a entrar acá y no se vuelva a pausar
			luigi.caer = True
			peleaPeach = True
			levantarLuigi = 30 #esta variable también se usará para que los movimientos de la princesa no sean tan rápidos


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_RIGHT and not marioDead and not win:
					mario.dir = 1
					mario.var_x = 5
					mario.var_basesprite = mario.sprite

				if event.key == pygame.K_LEFT and not marioDead and not win:
					mario.dir = 0
					mario.var_x = -5
					mario.var_basesprite = mario.sprite

				if event.key == pygame.K_SPACE and not marioDead and not win:
					if mario.estado == 3 and not mario.disparo:
						bola = FireBall(corteBola,suelos,mario.dir)
						bola.rect.center = mario.rect.center
						general.add(bola)
						bolasMario.add(bola)
						mario.disparo = True


				if event.key == pygame.K_UP and not marioDead:
					mario.salto()




			if event.type == pygame.KEYUP:

				if event.key == pygame.K_RIGHT and mario.var_x > 0:
					mario.var_x = 0

				if event.key == pygame.K_LEFT and mario.var_x < 0:
					mario.var_x = 0




		#colisión de las balas con los personajes:
		lCol = pygame.sprite.spritecollide(mario,bolasLuigi,True)
		for m in lCol:
			vidasMario -= 1
			print vidasMario
		lCol = pygame.sprite.spritecollide(luigi,bolasMario,True)
		for m in lCol:#se le tiene que restar uno a la vida de Luigi
			luigi.vida -= 1

		lCol = pygame.sprite.spritecollide(peach,bolasMario,True)
		for m in lCol:#se le tiene que restar uno a la vida de Peach
			peach.vidas -= 1

		#Colisión de la princesa con Mario
		lCol = pygame.sprite.spritecollide(peach,gMario,False)
		for m in lCol:
			if peach.dx > 0:#colisionó por la izquierda
				peach.beat(0)
			elif peach.dx < 0: #pega por la derecha
				peach.beat(1)

			if puntosPeach == 0:
				vidasMario -= 1
				puntosPeach = 4
			puntosPeach -= 1
			peach.dx = 0






		if vidasMario == 0:#Mario murió
			marioDead = True
			mario.var_x = 0
			#mario.var_y = 10
			#mario.gravedad()
			mario.rect.right = ANCHO - 20
			mario.rect.top = 0
			vidasMario = -1


		#MUERTE DE LA PRINCESA:

		if peach.dead:
			peach.rect.right = ANCHO - 40
			peach.rect.top = 0
			peach.dx = 0

		if peach.rect.top > ALTO:
			win = True


		#DIÁLOGOS CUANDO MARIO GANA
		if win:
			if tDialogoFF >= 0 and tDialogoFF < 90:
				BDF5 = True
				BDF6 = False

			if tDialogoFF >= 90 and tDialogoFF < 180:
				BDF5 = False
				BDF6 = True

			if tDialogoFF >= 180:
				BDF5 = False
				BDF6 = False

			tDialogoFF += 1

			mario.var_x = 5 # para que vaya y se tire en la lava
			mario.var_basesprite = mario.sprite
			mario.dir = 1
			mario.salto()







		pantalla.fill(NEGRO)
		pantalla.blit(Lakitu,[0,250])
		#fondos.update()
		#fondos.draw(pantalla)
		if not (BD1 or BD2 or BD3 or BD4 or BD5 or BD6 or BDF1 or BDF2 or BDF3 or BDF4 or BDF5 or BDF6):
			general.update()
			if mario.rect.top <= ALTO:
				gMario.update()
			else:
				fin = True
			#if luigi.vida != -1:#indica que Luigi desaparece de la pantalla
			if luigi.rect.top <= ALTO:#si ya cayó, no debe seguir actualizando
				gLuigi.update()
			if peleaPeach and peach.rect.top <= ALTO:#peach solo se mueve cuando van a pelear con ella
				gPeach.update()
			general.draw(pantalla)
			gMario.draw(pantalla)
			#if luigi.vida != -1:
			gLuigi.draw(pantalla)
			bolasMario.draw(pantalla)
			bolasLuigi.draw(pantalla)
			gPeach.draw(pantalla)

			tvidasLuigi = "Luigi: " + str(luigi.vida) + " vidas"
			tvidasMario = "Mario: " + str(vidasMario) + " vidas"
			tvidasPeach = "Peach: " + str(peach.vidas) + " vidas"
			if luigi.vida == -1:
				tvidasLuigi = "Luigi: 0 vidas"
			if vidasMario == -1:
				tvidasMario = "Mario: 0 vidas"
			font = pygame.font.SysFont("comicsansms",30)
			imgTMario = font.render(tvidasMario,1,BLANCO)
			imgTLuigi = font.render(tvidasLuigi,1,BLANCO)
			imgTPeach = font.render(tvidasPeach,1,BLANCO)
			pantalla.blit(imgTMario,[0,0])
			pantalla.blit(imgTLuigi,[200,0])
			pantalla.blit(imgTPeach,[400,0])
			

		if BD1:#primer diálogo
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(D1,[mario.rect.right,mario.rect.top - mario.rect.height])
			controllerMapa.dibujarFondo(3)


		if BD2:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(D2,[luigi.rect.left,luigi.rect.top - luigi.rect.height])

		if BD3:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(D3,[peach.rect.left,peach.rect.top - peach.rect.height])

		if BD4:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(D4,[0,150])

		if BD5:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(D5,[mario.rect.left,mario.rect.top - mario.rect.height])

		if BD6:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(D6,[luigi.rect.left,luigi.rect.top - luigi.rect.height])



		if BDF1:#primer diálogo final
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(DF1,[luigi.rect.left,luigi.rect.top - luigi.rect.height])

		if BDF2:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(DF2,[peach.rect.right,peach.rect.top - peach.rect.height])

		if BDF3:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(DF3,[mario.rect.right,mario.rect.top - mario.rect.height])

		if BDF4:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(DF4,[peach.rect.right,peach.rect.top - peach.rect.height])

		if BDF5:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(DF5,[mario.rect.right,mario.rect.top - mario.rect.height])

		if BDF6:
			general.draw(pantalla)
			gMario.draw(pantalla)
			gLuigi.draw(pantalla)
			gPeach.draw(pantalla)
			pantalla.blit(DF6,[0,150])


		pygame.display.flip()
		clock.tick(30)

	return win
