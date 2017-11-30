import pygame
import random




from Jugadores.Mario import Mario
from Objetos.Fireball import *

from configuraciones import *
mariopeque = 'Jugadores/imgJugador/pequemario.png'
mariogrande = 'Jugadores/imgJugador/mariogrande.png'
mariofuego = 'Jugadores/imgJugador/MarioFuego.png'
bolafuego = 'Objetos/boladefuego.png'

if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()


    jugadores = pygame.sprite.Group()
    general = pygame.sprite.Group()
    balasmario = pygame.sprite.Group()


    reloj = pygame.time.Clock()
    fin  = False


    jg = Mario(recortar(mariopeque,3,5),recortar(mariogrande,3,5),recortar(mariofuego,3,5))
    general.add(jg)
    jugadores.add(jg)



    f_x = 0
    f_varx = 0
    #para definir el liite que va el fondo, 0 es por un lado y -(ANCHOFONDO- ANCHOPANTALLA) es el limite de la derecha

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jg.dir = 1
                    jg.var_x = 1
                    jg.var_basesprite = jg.sprite


                if event.key == pygame.K_LEFT:
                    jg.dir = 0
                    jg.var_x = -1
                    jg.var_basesprite = jg.sprite

                if event.key == pygame.K_g:
                    #grandir
                    jg.crecer()

                if event.key == pygame.K_p:
                    #il va etre petite
                    jg.enano()

                if event.key == pygame.K_SPACE:
                    #print 'bola de fuego'
                    if jg.estado == 3 and not jg.disparo:
                        bola = FireBall(recortar(bolafuego,4,1), jg.dir)
                        bola.rect.x = jg.rect.x
                        bola.rect.y = jg.rect.y + 30
                        general.add(bola)
                        balasmario.add(bola)
                        jg.disparo = True




                if event.key == pygame.K_UP:
                    #jg.gritar()
                    jg.salto()
                    #jg.var_y = -10

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT and jg.var_x > 0:

                    jg.var_x = 0

                if event.key == pygame.K_LEFT and jg.var_x < 0:

                    jg.var_x = 0


                #jg.var_y = 0
                #if event.key == pygame.K_RIGHT  :
                    #jg.dir =0
                    #jg.var_x = 0
                #if event.key == pygame.K_LEFT   :
                    #jg.dir = 0
                    #jg.var_x = 0

        #ciclo de juego



        pantalla.fill(NEGRO)
        #pantalla.blit(fondo,[f_x,0])
        general.update()
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
        #f_x -= 1

            #f_x -= 1
