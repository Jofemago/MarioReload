import pygame
import random



from Jugadores.Mapa.MapaNivel1 import *
from Jugadores.Mario import Mario
from Objetos.Fireball import *
from Jugadores.Enemigos.Enemys import *
#Contiene un arreglo que provie
from Jugadores.Mapa.ControllerMapa import *
from Jugadores.Enemigos.ControllerEnemys import *

from configuraciones import *
mariopeque = 'Jugadores/imgJugador/pequemario.png'
mariogrande = 'Jugadores/imgJugador/mariogrande.png'
mariofuego = 'Jugadores/imgJugador/MarioFuego.png'
bolafuego = 'Objetos/boladefuego.png'
mariofuego = 'Jugadores/imgJugador/MarioFuego.png'
sabanamapas = 'Jugadores/Mapa/imgmapas/sabanamapas.png'


mapa = ConfiguracionJson('Jugadores/Mapa/jsonmapas/nivel2.json')

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
    pygame.display.set_caption("MARIO RELOAD")

    jugadores = pygame.sprite.Group()
    general = pygame.sprite.Group()
    balasmario = pygame.sprite.Group()
    Bonus = pygame.sprite.Group() #donde entraran todos los elementos que sean bonus (vidas, crecer, fuego)
    cuadros = pygame.sprite.Group() #todo tipo de cuadro, destruibles, bonus, monedas, invisibles
    esc = pygame.sprite.Group()
    EnemigosA =  pygame.sprite.Group() #Goomba
    EnemigosB =  pygame.sprite.Group() #carnivora
    #FUNCIONALIDADES DEL MAPA

    #GRUPOS DE ELEMENTO QUE HAY EN LA sabanamapas
    suelos = pygame.sprite.Group()
    fondos =  pygame.sprite.Group()

    mario = Mario(recortar(mariopeque,4,5),recortar(mariogrande,4,5),recortar(mariofuego,4,5))
    #general.add(mario)
    jugadores.add(mario)

    #SE VA ENCARGAR DE IR DIBUJANDO EL MAPA A MEDIDA QUE VA AVANZADO MARIO
    sabanaMapa = recortar(sabanamapas,10,10)
    controllerMapa = MakeMapa(mapa,sabanaMapa,suelos,fondos,general,cuadros,Bonus )
    controllerMapa.dibujarFondo(2)
    controllerMapa.dibujarmapa()

    controllerEnemigos = MakeEnemys(mapa, sabanaMapa, EnemigosA, EnemigosB,suelos, general)
    controllerEnemigos.dibujarmapa()
    reloj = pygame.time.Clock()
    fin  = False



    Escombros = recortar( 'Jugadores/Mapa/imgmapas/escombros2.png',4,1)


    imgsuelo = 'Jugadores/Mapa/imgmapas/prueba.png'

    #configuracion de mapa
    mario.suelos = suelos
    #mario.Enemigos = Enemigos
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
        f_varx = limiteMovMario(mario, limitemario)#calculo de la pos del mario
        f_x  = moverFondo(f_x, f_varx) #ubicacion en el archivo json

        moverGrupoSprites(suelos, f_varx)#mueve todo lo que sea suelo, sabanamapas[0][0]
        moverGrupoSprites(Bonus, f_varx)
        moverGrupoSprites(esc, f_varx)
        moverGrupoSprites(EnemigosA, f_varx)
        moverGrupoSprites(EnemigosB, f_varx)

        #VALIDA SI CADA CUADRO TIENE QUE CREAR EL BONUS AL CUAL MARIO HA GOLPEADO
        for c in cuadros:
            if c.crear:

                if c.create == "poder":
                    #print "si"
                    if mario.estado == 1:
                        p = PoderHongo(mario.estado, c.rect.x, c.rect.y,suelos)
                        general.add(p)
                        Bonus.add(p)
                    else:
                        p = PoderFuego(mario.estado, c.rect.x, c.rect.y)
                        general.add(p)
                        Bonus.add(p)
                    c.crear = False
                if c.create == "vivir":
                    p = VidaHongo(mario.estado, c.rect.x, c.rect.y,suelos)
                    general.add(p)
                    Bonus.add(p)
                    c.crear = False

                if c.create == "moneda":
                    p = MonedaCuadro( c.rect.x, c.rect.y - 40)
                    print 'Ganaste moneda por darle al cuadro'
                    general.add(p)
                    Bonus.add(p)
                    #Bonus.add(k)
                    #general.add(k)
                    c.crear = False
                if c.create == "monedasladrillo":
                    p = MonedaCuadro( c.rect.x, c.rect.y - 40)
                    print 'Ganaste moneda por darle al ladrillo'
                    general.add(p)
                    Bonus.add(p)
                    #Bonus.add(k)
                    #general.add(k)
                    c.crear = False

                if c.create == "ladrillo":
                    if c.destruir():
                        e = escombro(c.rect.x -20, c.rect.y - 50 -20 ,Escombros[0][0],-1)
                        esc.add(e)
                        general.add(e)
                        e = escombro(c.rect.x+20, c.rect.y -50 -20 ,Escombros[1][0],1)
                        esc.add(e)
                        general.add(e)
                        e = escombro(c.rect.x-10, c.rect.y -20 ,Escombros[2][0],-1)
                        general.add(e)
                        esc.add(e)
                        e = escombro(c.rect.x+10, c.rect.y -20 ,Escombros[3][0],1)
                        general.add(e)
                        esc.add(e)
                        #fondos.add(e)

                        c.kill()


                    c.crear = False
        #colision de mario con los bonus
        ls_col = pygame.sprite.spritecollide(mario, Bonus, True)
        if len(ls_col) > 0:
            for e in ls_col:
                if e.efecto == 'fuego': #evento que consigue el mario fuego
                    mario.bonus += e.bonus
                    mario.crecer()
                if e.efecto == "crecer":
                    mario.bonus += e.bonus
                    mario.crecer()
                if e.efecto == "vida":
                    mario.bonus += e.bonus
                    mario.vidas += 1
                    print 'Has ganado una vida'
                if e.efecto == "moneda":
                    mario.bonus += e.bonus
                    print "ganaste moneda"
                    e.kill()



        #CONFIGURACION DE LOS ENEMIGOS
        ls_col = pygame.sprite.spritecollide(mario, EnemigosA, False)
        if len(ls_col) > 0:
            for e in ls_col:
                if not e.golpe:
                    if mario.saltar :
                        e.golpe = True
                        print 'salto'
                    else:
                        if mario.estado == 1 and not mario.inmune:
                            #mario.salto()
                            mario.var_y = 7
                            mario.morir = True

                        else :
                            mario.enano()
                            mario.inmune = True

        ls_col = pygame.sprite.spritecollide(mario, EnemigosB, False)
        if len(ls_col) > 0:
            for e in ls_col:
                if e.i != 0:
                    if mario.estado == 1 and not mario.inmune and not mario.morir:
                        #mario.salto()

                        mario.var_y = 7
                        mario.morir = True

                    else :
                        mario.enano()
                        mario.inmune = True



        for b in balasmario:
            s_col = pygame.sprite.spritecollide(b, EnemigosA, True)
            s_col = pygame.sprite.spritecollide(b, EnemigosB, False)
            if len(s_col) > 0:
                for e in s_col:
                    if e.i != 0:
                        e.kill()

        if mario.rect.y > ALTO:
            return [False, mario.vidas]

        pantalla.fill(NEGRO)
        #pantalla.blit(fondo,[f_x,0])
        fondos.update()
        fondos.draw(pantalla)
        general.update()
        jugadores.update()
        general.draw(pantalla)
        jugadores.draw(pantalla)
        EnemigosA.draw(pantalla)
        balasmario.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)




if __name__ =='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO, ALTO])
    pygame.display.flip()
    l = Nivel1(pantalla)
    print l
