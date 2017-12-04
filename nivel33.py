import pygame
import random



from Jugadores.Mapa.MapaNivel1 import *
from Jugadores.Mario import Mario
from Objetos.Fireball import *
#Contiene un arreglo que provie
from Jugadores.Mapa.ControllerMapa import *


from configuraciones import *
mariopeque = 'Jugadores/imgJugador/pequemario.png'
mariogrande = 'Jugadores/imgJugador/mariogrande.png'
mariofuego = 'Jugadores/imgJugador/MarioFuego.png'
bolafuego = 'Objetos/boladefuego.png'
mariofuego = 'Jugadores/imgJugador/MarioFuego.png'
sabanamapas = 'Jugadores/Mapa/imgmapas/sabanamapas.png'

mapa = ConfiguracionJson('Jugadores/Mapa/jsonmapas/nivel3.json')
def limiteMovMario(mario, limitemario):

    #valida cuando es el momneto de mover el mapa de mario
    if mario.rect.x  > limitemario - mario.rect.width:
        mario.rect.x = limitemario - mario.rect.width
        return -5
    else:
        return 0


def moverGrupoSprites(grupo, f_varx):
    #define como mover un grupo especifico
    for s in grupo:
        s.rect.x += f_varx


def moverFondo(fx, varx):
    #mover el fondo
    return fx+varx

def Nivel1(pantalla):



    jugadores = pygame.sprite.Group()
    general = pygame.sprite.Group()
    balasmario = pygame.sprite.Group()

    #FUNCIONALIDADES DEL MAPA

    #GRUPOS DE ELEMENTO QUE HAY EN LA sabanamapas
    suelos = pygame.sprite.Group()
    fondos =  pygame.sprite.Group()

    mario = Mario(recortar(mariopeque,3,5),recortar(mariogrande,3,5),recortar(mariofuego,3,5))
    #general.add(mario)
    jugadores.add(mario)

    #SE VA ENCARGAR DE IR DIBUJANDO EL MAPA A MEDIDA QUE VA AVANZADO MARIO
    controllerMapa = MakeMapa(mapa,recortar(sabanamapas,10,10),suelos,fondos,general )
    controllerMapa.dibujarmapa()

    reloj = pygame.time.Clock()
    fin  = False





    imgsuelo = 'Jugadores/Mapa/imgmapas/prueba.png'

    #configuracion de mapa
    mario.suelos = suelos
    '''
    for i in range(0,z):
        m = suelo(imgsuelo)
        m.setpos(i*40 , y)
        suelos.add(m)
        general.add(m)
    '''



    f_x = 0
    f_varx = 0
    limitemario = 400
    #para definir el liite que va el fondo, 0 es por un lado y -(ANCHOFONDO- ANCHOPANTALLA) es el limite de la derecha

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mario.dir = 1
                    mario.var_x = 1
                    mario.var_basesprite = mario.sprite


                if event.key == pygame.K_LEFT:
                    mario.dir = 0
                    mario.var_x = -1
                    mario.var_basesprite = mario.sprite

                if event.key == pygame.K_g:
                    #grandir
                    mario.crecer()

                if event.key == pygame.K_p:
                    #il va etre petite
                    mario.enano()

                if event.key == pygame.K_SPACE:
                    #print 'bola de fuego'
                    if mario.estado == 3 and not mario.disparo:
                        bola = FireBall(recortar(bolafuego,4,1),suelos ,mario.dir)
                        bola.rect.x = mario.rect.x
                        bola.rect.y = mario.rect.y + 30
                        general.add(bola)
                        balasmario.add(bola)
                        mario.disparo = True




                if event.key == pygame.K_UP:
                    #mario.gritar()
                    mario.salto()
                    #mario.var_y = -10

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT and mario.var_x > 0:

                    mario.var_x = 0

                if event.key == pygame.K_LEFT and mario.var_x < 0:

                    mario.var_x = 0


                #mario.var_y = 0
                #if event.key == pygame.K_RIGHT  :
                    #mario.dir =0
                    #mario.var_x = 0
                #if event.key == pygame.K_LEFT   :
                    #mario.dir = 0
                    #mario.var_x = 0

        #ciclo de juego

        #proceso para mario recorra el mapa unicamente de izquierda a derecha
        #f_varx = limiteMovMario(mario, limitemario)#calculo de la pos del mario
        #f_x  = moverFondo(f_x, f_varx) #ubicacion en el archivo json

        #moverGrupoSprites(suelos, f_varx)#mueve todo lo que sea suelo, sabanamapas[0][0]


        pantalla.fill(NEGRO)
        #pantalla.blit(fondo,[f_x,0])
        general.update()
        jugadores.update()
        general.draw(pantalla)
        jugadores.draw(pantalla)
        balasmario.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)



if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()
    Nivel1(pantalla)
