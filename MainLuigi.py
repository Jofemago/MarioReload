import pygame
import random

from Jugadores.Luigi import *
from configuraciones import *
from Objetos.Fireball import *

if (__name__ == '__main__'):
    pygame.init()


    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.flip()
    imgbola = 'Objetos/boladefuego.png'
    recorteBola = recortar(imgbola,4,1)
    jugadores = pygame.sprite.Group()
    general = pygame.sprite.Group()
    cuts = recortar('Jugadores/imgJugador/luigi.png',4,4)
    jugador = Luigi(cuts)
    jugador.rect.x = CENTRO[0]
    jugador.rect.y = CENTRO[1]
    jugadores.add(jugador)
    bolas = pygame.sprite.Group()
    general.add(jugador)
    clock = pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    jugador.left()

                if event.key == pygame.K_RIGHT:
                    jugador.right()

                if event.key == pygame.K_UP:
                    jugador.jump()


            if event.type == pygame.KEYUP:
                jugador.keyup()


        if jugador.disparo:
            if jugador.dir == 0:#va para la derecha
                bola = FireBall(recorteBola,1)
            else:#izquierda
                bola = FireBall(recorteBola,0)
            bola.rect.center = jugador.rect.center
            #bola.rect.y = jugador.rect.y
            bolas.add(bola)
            general.add(bola)



        general.update()
        pantalla.fill(NEGRO)
        general.draw(pantalla)
        pygame.display.flip()
        clock.tick(30)

