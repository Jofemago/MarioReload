import pygame
import random

from Jugadores.Peach import *
from configuraciones import *

if (__name__ == '__main__'):
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.flip()
    jugadores = pygame.sprite.Group()
    cuts = recortar('Jugadores/imgJugador/peach.png',4,4)
    jugador = Peach(cuts)
    jugador.rect.x = CENTRO[0]
    jugador.rect.y = CENTRO[1]
    jugadores.add(jugador)
    clock = pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    jugador.dir = 1
                    jugador.dx = -5

                if event.key == pygame.K_RIGHT:
                    jugador.dir = 0
                    jugador.dx = 5

                if event.key == pygame.K_UP:
                    jugador.dy = -5

                if event.key == pygame.K_SPACE:
                    if jugador.dir == 0:
                        jugador.dir = 2

                    if jugador.dir == 1:
                        jugador.dir = 3


            if event.type == pygame.KEYUP:

                jugador.dx = 0
                jugador.dy = 0


        jugadores.update()
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        clock.tick(30)
