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
                    jugador.left()

                if event.key == pygame.K_RIGHT:
                    jugador.right()

                if event.key == pygame.K_UP:
                    jugador.jump()

                if event.key == pygame.K_SPACE:
                    jugador.beat()


            if event.type == pygame.KEYUP:
            	jugador.keyup(event.key)


        jugadores.update()
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        clock.tick(30)
