import pygame
from configuraciones import *
from Objetos.Fireball import *
from Jugadores.MapaNivel1 import *
class Mario(pygame.sprite.Sprite):

    def __init__(self,imgpeque,imggrande, imgfuego = None, col = AZUL):

        pygame.sprite.Sprite.__init__(self)
        self.m = imgfuego


        self.imgpeque = imgpeque
        self.imggrande = imggrande
        self.imgfuego = imgfuego
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.setPos(100,0)


        #estado para saber que mario es, peque fuego o grande
        self.estado = 1

        #variables para los movimientos de sprites
        self.dir = 0
        self.i = 0

        #valor de la gravedad
        self.g = -15
        #controla la velocidad de movimiento en X
        self.vel_x = 0.07

        #Velocidad de actualiza
        self.sprite = 4
        self.var_basesprite = self.sprite
        self.var_sprite = self.var_basesprite

        #variables de movimiento
        self.var_x =  0
        self.var_y = 0

        #variable que calcula el salto de el mario significa que en faso
        self.saltar = False
        #self.vidas = vidas
        self.plataformas =  None
        self.suelos = pygame.sprite.Group()
        self.col = False


        #control de disparo
        self.disparo = False
        self.tiempodis = 20 # tiempo que debe esperar despues de dispara para seguir disparando
        self.controldis = self.tiempodis#tiempo que se reducria


    def disparar(self):

        if  self.disparo:

            if self.controldis <=0:
                self.disparo = False
                self.controldis = self.tiempodis
            self.controldis -= 1


    def setPos(self, x,  y):

        self.rect.x = x
        self.rect.y = y

    def setX(self, x):

        self.rect.x = x

    def setX(self, y):

        self.rect.x = y

    def movX(self):

        if self.rect.x >= ANCHO -self.rect.width and self.var_x >= 0:
            self.var_x = 0

        if self.rect.x <= 0 and self.var_x <= 0:
            self.var_x = 0


        #self.rect.x += self.var_x

    def movY(self):


        if self.rect.y >= ALTO - self.rect.height and self.var_y >= 0:
            self.var_y = 0
            self.saltar = False

        if self.rect.y <= 100 and self.var_y <= 0:
            self.var_y = 0
            #self.saltar = False




        #self.rect.y += self.var_y


    def gravedad(self):

        #si no hya colision que empiece a bajar haciendo efecto de gravedad
        if not self.col:
            if self.var_y == 0:
                self.var_y = 1
            else:
                self.var_y += 1

        #bordes
        #if self.rect.y >= ALTO - self.rect.height  and self.var_y >= 0:
        #    self.var_y = 1
        #    self.saltar = False
        #    self.rect.y = ALTO - self.rect.height




    def salto(self):
        if not self.saltar:
            if self.var_x <= 0:
                self.var_y = self.g + self.var_x/2*2 #haga la variable de salto y mueva elsprite hasta la posicion indicada
                #self.var_x =-1
            else:
                self.var_y = self.g - self.var_x/2*2
                #self.var_x =1
            #else:
            #    self.var_y = -7
            self.saltar = True
            #este mientras sube ira perdiendo la altura con la gravedad activa

    def gritar(self):
        #self.sonido.play()
        pass

    def validarColision(self):

        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:# si de verdad hay colision
            for m in ls_bl:#otra solucion es que cuando toque por la parte de ariba del objeto la variacion en y sea 0

                if self.var_x > 0:
                    self.rect.right = m.rect.left
                    self.col = True # haga colision true para que no afecte la gravedad
                    #self.gravedad()
                elif self.var_x < 0:
                    self.rect.left  = m.rect.right
                    self.col = True
                    #self.gravedad()
        else:
            self.col = False# si no hay colision active de nuevo la gravedad

        self.rect.y += self.var_y   #para que siempre juegue la gravedad
        ls_bl = pygame.sprite.spritecollide(self,self.suelos, False)
        if len(ls_bl) > 0:
            for m in ls_bl:
                if self.var_y > 0:
                    self.rect.bottom = m.rect.top
                    #como choca no puede estar en sprite de salto, esta montado en una platafoma
                    self.saltar = False
                    self.col = True


                elif self.var_y < 0:
                    self.rect.top  = m.rect.bottom
                    self.var_y = 0
                    self.col = True
        else:
            self.col = False


    #SE ENCARGA DEL MOVIMIENTO TANTO COMO DEL SPRITE COMO DE INCREMETAR EL MOVMINETO DEL JUGADOR
    def movSprite(self):

        if self.var_sprite <= 0:
            if self.var_x != 0:
                if self.i < 2 :

                    self.i += 1
                else:
                    self.i = 0
            else:
                self.i = 0
            self.var_sprite = self.var_basesprite
        self.var_sprite -= 1


        if self.saltar:
            self.image = self.m[self.i][self.dir+2]
        else:
            self.image = self.m[self.i][self.dir]
        #self.rect = self.image.get_rect()
        self.rect.x += self.var_x

    #Se encarga de controlar la velocidad con la que se mueve mario en el X va ir aumentando a medida que este se mueva
    def aumentoVelocidad(self):


        if self.var_x >= -5 and self.var_x <= 5:
            if self.var_x != 0:

                if self.var_x > 0:
                    self.var_x += self.vel_x
                    self.var_basesprite -= self.vel_x/3
                else:
                    self.var_x -= self.vel_x
                    self.var_basesprite -= self.vel_x/3

    #hace crecer a mario
    def crecer(self):

        if  self.estado < 3:
            if self.estado == 1:
                self.rect.y -= 60
            self.estado += 1


    #hacer enchiquetecer a mario
    def enano(self):
        self.estado = 1

    #validar que juego de sprites debe tomar mario dependiendo de su estado
    def validarImagen(self):

        if self.estado == 3:
            self.m = self.imgfuego
        elif self.estado == 2:
            self.m = self.imggrande
        else:
            self.m = self.imgpeque

        if self.saltar:
            self.image = self.m[self.i][self.dir+2]
        else:
            self.image = self.m[self.i][self.dir]

        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):

        self.movX()
        #self.rect.y += self.var_y

        self.aumentoVelocidad()

        self.gravedad()
        #colisiones
        self.validarColision()

        #movimiento de los sprites
        self.movSprite()

        #validamos siempre de que tamano es mario
        self.validarImagen()

        # si se ha disparado espera un momento corto para volverlo a hacer
        self.disparar()
