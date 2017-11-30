import pygame

from Fireball import *
from configuraciones import *

if (__name__ == '__main__'):
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.flip()
    bolas = pygame.sprite.Group()
    cuts = recortar('boladefuego.png',4,1)
    bola = FireBall(cuts)
    bola.rect.x = 0
    bola.rect.y = ALTO - 200
    bolas.add(bola)
    clock = pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        if bola.rect.bottom >= ALTO:
            bola.rebotar() #esta es solo una prueba. En el caso del juego, se rebota cada vez que colisiones con el suelo


        bolas.update()
        pantalla.fill(NEGRO)
        bolas.draw(pantalla)
        pygame.display.flip()
        clock.tick(30)
