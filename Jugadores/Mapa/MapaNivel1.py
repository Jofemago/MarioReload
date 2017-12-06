
#EN este archivo se crea el elemento 1 de la sabanamapas
import pygame
from configuraciones import *

class base(pygame.sprite.Sprite):

    def __init__(self, archivo):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(archivo).convert_alpha()
        self.image = archivo
        self.rect= self.image.get_rect()

    def setpos(self,x ,y):
        self.rect.x = x
        self.rect.y = y

    def getTipo(self):
        return 'nada'

    def update(self):
        pass


class suelo(base):

    def __init__(self, archivo):
        base.__init__(self,archivo)


class lava(pygame.sprite.Sprite):

    def __init__(self,x , y):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar('Jugadores/Mapa/imgmapas/lava.png',9,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.setPos(x,y)
        self.i = 0
        self.timesprite = 5
        self.actualizasprite = self.timesprite

    def getTipo(self):
        return 'lava'

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y


    def updateSprite(self):

        self.image = self.m[self.i][0]

    def movSprite(self):


        if self.actualizasprite < 0:
            if self.i < 7 :
                self.i += 1
            else:
                self.i = 0
            self.actualizasprite = self.timesprite
        self.actualizasprite -= 1



    def update(self):

        self.movSprite()
        self.updateSprite()


class bonus(pygame.sprite.Sprite):

    def __init__(self,x , y, archivo, f, c):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar(archivo,f,c)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.setPos(x,y)
        self.posy = y #posicion inicial de y
        self.i = 0
        self.timesprite = 10
        self.actualizasprite = self.timesprite


        #elemento que dice si va crear o no, si algun sprite no crea se le incializara crearte en False
        self.crear = False

        #ACA VALIDA LAS COLISIONES
        self.golpe = False #valida con esto si el el mario ha chocado con el
        self.golpazo = False
        self.estadoMario = 1 #valida en que estado esta mario para ver que tiene que hacer en este estado


    def getTipo(self):
        return 'bonus'

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y

    def modificarEstado(self, estadomario):
        self.golpe = True
        self.estadoMario = estadomario
        self.golpazo = True

    def updateSprite(self):


        self.image = self.m[self.i][0]

    def movSprite(self):

        if not self.golpe:
            if self.actualizasprite < 0:
                if self.i < 2 :
                    self.i += 1
                else:
                    self.i = 0
                self.actualizasprite = self.timesprite
            self.actualizasprite -= 1
        else:
            self.i = 3

    def gravedad(self):

        if self.rect.y < self.posy:
            self.rect.y += 2

    def update(self):
        #print self.golpe
        self.movSprite()
        self.updateSprite()
        self.gravedad()
        if self.golpazo :
            self.rect.y -= 14
            self.golpazo = False



#ESTE BONUS CREARA UN HONGO DE CRECIMIENTO O UNA PLATA DE FUEGO
class bonuspoder(bonus):

    def __init__(self, x, y):
        bonus.__init__(self,x , y,'Jugadores/Mapa/imgmapas/bonus.png',4,1)
        self.create = "poder"#significa que se creara una hongo de crecimiento o un poder en fuego dependiendo del estado del mario
        self.estadoBonus = 0



    def update(self):
        bonus.update(self)

        if self.golpe == True and self.estadoBonus == 0:

            self.estadoBonus += 1
            self.crear = True

class bonusVida(bonus):

    def __init__(self,x , y,archivo):
        bonus.__init__(self,x , y,archivo,2,1)
        self.create = "vivir"#significa que se creara una hongo de crecimiento o un poder en fuego dependiendo del estado del mario
        self.estadoBonus = 0


    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y

    def movSprite(self):

        if not self.golpe:
            self.i = 0
        else:
            self.i = 1

    def update(self):
        bonus.update(self)

        if self.golpe == True and self.estadoBonus == 0:

            self.estadoBonus += 1
            self.crear = True


class bonusMoneda(bonus):

    def __init__(self, x, y):
        bonus.__init__(self,x , y,'Jugadores/Mapa/imgmapas/bonus.png',4,1)
        self.create = "moneda"#significa que se creara una hongo de crecimiento o un poder en fuego dependiendo del estado del mario
        self.estadoBonus = 0

    def update(self):
        bonus.update(self)

        if self.golpe == True and self.estadoBonus == 0:

            self.estadoBonus += 1
            self.crear = True





#Objetos que salen de de los bonus

class Hongo(pygame.sprite.Sprite):

    def __init__(self, estado,x,y,suelos, archivo,an, al):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar(archivo,an,al)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.bonus = 100 #cantidad de puntos que entrega esta hazana

        #self.efecto = "crecer"

        self.estado = estado #estado del mario pra saber que crea
        self.setPos(x,y - 40)

        self.crecer = True #variable de crecimiento del hongo
        self.i = 0

        self.var_basesprite = 2 # cada cuanto se activa el sprite
        self.var_sprite = self.var_basesprite

        #movimiento en el mapa
        self.dir = 2 #va de izquierda a derecha inicialmente
        self.var_x = 3
        self.var_y = 0
        self.col = False
        self.suelos = suelos


    def gravedad(self):

        #si no hya colision que empiece a bajar haciendo efecto de gravedad
        if not self.col:
            if self.var_y == 0:
                self.var_y = 1
            else:
                self.var_y += 1


    def validarColision(self):
        self.rect.x += self.var_x
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:# si de verdad hay colision
            for m in ls_bl:#otra solucion es que cuando toque por la parte de ariba del objeto la variacion en y sea 0

                if self.var_x > 0:
                    self.rect.right = m.rect.left
                    self.dir = 1
                    self.col = True # haga colision true para que no afecte la gravedad
                    #self.gravedad()
                elif self.var_x < 0:
                    self.rect.left  = m.rect.right
                    self.dir  = 2
                    self.col = True

                    #self.rect.x += self.var_x
                    #self.gravedad()
        else:
            self.col = False# si no hay colision active de nuevo la gravedad

        self.rect.y += self.var_y   #para que siempre juegue la gravedad
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:
            for m in ls_bl:
                if self.var_y > 0:
                    self.rect.bottom = m.rect.top -5
                    #como choca no puede estar en sprite de salto, esta montado en una platafoma
                    #self.saltar = False
                    self.col = True



                elif self.var_y < 0:
                    self.rect.top  = m.rect.bottom


                    self.var_y = 0
                    self.col = True
        else:
            self.col = False


    def CrecerSprite(self):

        if self.crecer:
            #print self.var_sprite
            #mientras crece sube el lvl este prooo
            if self.var_sprite <= 0:

                if self.i < 4 :
                    self.i += 1
                if self.i == 4:
                    self.crecer = False
                    #self.rect.x += 100

                self.var_sprite = self.var_basesprite
            self.var_sprite -= 1

    def ubicarimg(self):
        self.image = self.m[self.i][0]


    def movimientoX(self):
        #print self.dir
        if self.dir == 2:
            self.var_x = 3
        else:
            self.var_x = -3

    def setPos(self,x,y):

        self.rect.x = x
        self.rect.y = y

    def destruir(self):

        if self.rect.y >= ANCHO:
            self.kill()
    def update(self):

        self.CrecerSprite()
        self.ubicarimg()

        self.gravedad()
        self.movimientoX()
        self.validarColision()
        self.destruir()

class PoderHongo(Hongo):

    def __init__(self,estado,x,y,suelos):
        Hongo.__init__(self, estado,x,y,suelos, 'Jugadores/Mapa/imgmapas/hongo.png', 5, 1)
        self.efecto = "crecer"

class VidaHongo(Hongo):

    def __init__(self,estado,x,y,suelos):
        Hongo.__init__(self, estado,x,y,suelos, 'Jugadores/Mapa/imgmapas/vida.png', 5, 1)
        self.efecto = "vida"
#--------------------------------------------
class PoderFuego(pygame.sprite.Sprite):

    def __init__(self, estado,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar('Jugadores/Mapa/imgmapas/fuego.png',5,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.bonus = 200 #cantidad de puntos que entrega esta hazana

        self.efecto = "fuego"

        self.estado = estado #estado del mario pra saber que crea
        self.setPos(x,y - 25)

        self.crecer = True #variable de crecimiento del hongo
        self.i = 0

        self.var_basesprite = 2 # cada cuanto se activa el sprite
        self.var_sprite = self.var_basesprite


    def CrecerSprite(self):

        if self.crecer:
            #print self.var_sprite
            #mientras crece sube el lvl este prooo
            if self.var_sprite <= 0:

                if self.i < 4 :
                    self.i += 1
                if self.i == 4:
                    self.crecer = False

                self.var_sprite = self.var_basesprite
            self.var_sprite -= 1

    def ubicarimg(self):

        self.image = self.m[self.i][0]


    def setPos(self,x,y):

        self.rect.x = x
        self.rect.y = y

    def update(self):

        self.CrecerSprite()
        self.ubicarimg()

class Moneda(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar('Jugadores/Mapa/imgmapas/moneda.png',4,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.bonus = 150 #cantidad de puntos que entrega esta hazana

        self.efecto = "moneda"

        self.i = 0
        self.var_basesprite = 8 # cada cuanto se activa el sprite
        self.var_sprite = self.var_basesprite
        self.setPos(x,y)

    def MovimientoSprite(self):

        if self.var_sprite <= 0:

            if self.i <  3:
                self.i += 1
            else:
                self.i = 0
                #self.rect.x += 100

            self.var_sprite = self.var_basesprite
        self.var_sprite -= 1

    def ubicarimg(self):
        self.image = self.m[self.i][0]

    def setPos(self,x,y):

        self.rect.x = x
        self.rect.y = y

    def destruir(self):

        if self.rect.y > ANCHO:
            self.kill

    def update(self):

        self.MovimientoSprite()
        self.ubicarimg()
        self.destruir()



class MonedaCuadro(Moneda):

    def __init__(self,x,y):

        Moneda.__init__(self,x,y)
        #self.rect.y -= 70
        self.posini = y
        self.pos = False
        self.g = 10
        self.saltar = False


    def salto(self):
        if not self.saltar:
            self.var_y = self.g
        if self.rect.y < self.posini - 70:
            self.saltar = True



    def caer(self):
        if  self.saltar:
            self.var_y = -10


    def gravedad(self):
        self.rect.y += 0.25

    def update(self):
        Moneda.update(self)
        self.salto()
        self.caer()
        self.rect.y -= self.var_y
        #self.var_y = 0
        #self.saltar = True

        self.gravedad()

        if self.rect.y > self.posini:
            self.kill()


class MuroMonedas(pygame.sprite.Sprite):

    def __init__(self,x , y ,archivo):
        pygame.sprite.Sprite.__init__(self)
        self.m = recortar(archivo,2,1)
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.setPos(x,y)
        self.posy = y #posicion inicial de y
        self.i = 0
        #self.timesprite = 10
        #self.actualizasprite = self.timesprite
        self.create = "monedasladrillo"

        #elemento que dice si va crear o no, si algun sprite no crea se le incializara crearte en False
        self.crear = False

        #ACA VALIDA LAS COLISIONES
        self.golpe = False #valida con esto si el el mario ha chocado con el
        self.golpazo = False
        self.estadoMario = 1 #valida en que estado esta mario para ver que tiene que hacer en este estado

        self.monedas = 4
        self.monedasobtenidas = 0

    def getTipo(self):
        return 'bonus'

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y

    def modificarEstado(self, estadomario):
        self.golpe = True
        self.estadoMario = estadomario
        self.golpazo = True

    def updateSprite(self):


        self.image = self.m[self.i][0]

    def movSprite(self):

        if self.monedasobtenidas >= self.monedas:
            self.i = 1
        else:
            self.i = 0

    def gravedad(self):

        if self.rect.y < self.posy:
            self.rect.y += 2

    def update(self):
        #print self.golpe
        self.movSprite()
        self.updateSprite()
        self.gravedad()
        if self.golpazo :
            self.rect.y -= 14
            self.golpazo = False

        if self.golpe == True and self.monedasobtenidas < self.monedas:

            self.monedasobtenidas += 1
            self.crear = True
            self.golpe = False



class MuroLadrillos(pygame.sprite.Sprite):

    def __init__(self,x , y ,archivo):
        pygame.sprite.Sprite.__init__(self)

        self.image = archivo
        self.rect = self.image.get_rect()
        self.setPos(x,y)
        self.posy = y #posicion inicial de y
        #self.timesprite = 10
        #self.actualizasprite = self.timesprite
        self.create = "ladrillo"

        #elemento que dice si va crear o no, si algun sprite no crea se le incializara crearte en False
        self.crear = False

        #ACA VALIDA LAS COLISIONES
        self.golpe = False #valida con esto si el el mario ha chocado con el
        self.golpazo = False
        self.estadoMario = 1 #valida en que estado esta mario para ver que tiene que hacer en este estado


    def getTipo(self):
        return 'bonus'

    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y

    def modificarEstado(self, estadomario):

        self.estadoMario = estadomario
        self.golpe = True
        self.golpazo = True
        #self.crear = True

    def gravedad(self):

        if self.rect.y < self.posy:
            self.rect.y += 2

    def destruir(self):

        if self.estadoMario > 1:
            return True
        else:
            return False

    def update(self):
        #print self.golpe

        self.gravedad()
        if self.golpazo :
            self.rect.y -= 14
            self.golpazo = False
            self.crear = True


class escombro(pygame.sprite.Sprite):

    def __init__(self,x , y, archivo, vel_x):

        pygame.sprite.Sprite.__init__(self)

        self.image = archivo
        self.rect = self.image.get_rect()

        self.vel_x = vel_x
        self.setPos(x,y)
        self.vary = 0.2


    def setPos(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.vary += 0.2
        self.rect.y += 5 +self.vary
        self.rect.x += self.vel_x
        if self.rect.y > ALTO-100:
            self.kill()
