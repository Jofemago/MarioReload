
import pygame
from MapaNivel1 import *
from configuraciones import *


class MakeMapa:

    def __init__(self,mapa ,sabana,suelos,fondos,general,cuadros,Bonus):

        self.mapa = mapa
        #print mapa
        self.sabana = sabana
        self.filas = len(self.mapa)
        self.col = len(self.mapa[0])
        self.suelos = suelos#controlar donde el personaje solo puede pisar
        self.fondos = fondos #se guardaran los fonsdos aqui
        self.general = general#controlatodo
        self.cuadros = cuadros #todo tipo de cuadros que al golpear mario den bonus
        self.Bonus = Bonus
        #self.nivel = nivel
        #print self.filas, self.col

    def dibujarFondo(self, nivel):
        #dibuja un fondo dependiendo del nivel especifico
        for j in range(ANCHO /40):
            for i in range(1,ALTO /40):
                if nivel == 1:
                    #print 'hola'
                    m = suelo(self.sabana[3][0])
                    m.setpos(j*40 , i*40)
                    self.fondos.add(m)
                    #self.general.add(m)
                if nivel == 2:
                    pass
                if nivel == 3:
                    m = suelo(self.sabana[1][9])
                    m.setpos(j*40 , i*40)
                    self.fondos.add(m)


    def dibujarmapa(self):
        for i in range(self.filas):
            for j in range(self.col):

                #se dibujan suelos
                if self.mapa[i][j] == 1 :
                    m = suelo(self.sabana[0][0])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 2 :
                    m = MuroLadrillos(j*40 , i*40,self.sabana[1][0])
                    self.cuadros.add(m)
                    self.suelos.add(m)
                    self.general.add(m)
                #Signo de interrogacion  BONUS
                if self.mapa[i][j] == 3 :
                    m = bonuspoder(j*40 , i*40)
                    #m.golpe = True
                    self.cuadros.add(m)
                    self.suelos.add(m)
                    self.general.add(m)

                #Bonus
                if self.mapa[i][j] == 5 :
                    m = bonusVida(j*40 , i*40)
                    #m.golpe = True
                    self.cuadros.add(m)
                    self.suelos.add(m)
                    self.general.add(m)

                #monedas
                if self.mapa[i][j] == 6 :
                    m = Moneda(j*40 , i*40)
                    #m.golpe = True
                    #self.cuadros.add(m)
                    #self.suelos.add(m)
                    self.Bonus.add(m)
                    self.general.add(m)

                #Bonus moneda
                #monedas
                if self.mapa[i][j] == 7 :
                    m = bonusMoneda(j*40 , i*40)
                    #m.golpe = True
                    self.cuadros.add(m)
                    self.suelos.add(m)
                    #self.Bonus.add(m)
                    self.general.add(m)

                #ladrillos de monedas
                if self.mapa[i][j] == 8 :
                    m = MuroMonedas(j*40 , i*40)
                    #m.golpe = True
                    self.cuadros.add(m)
                    self.suelos.add(m)
                    #self.Bonus.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 9 :
                    m = suelo(self.sabana[8][0])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 11 :
                    m = suelo(self.sabana[0][1])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 12 :
                    m = suelo(self.sabana[1][1])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 13 :
                    m = suelo(self.sabana[2][1])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 14:
                    m = suelo(self.sabana[3][1])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                #TERCER NIVEL
                #Suelo
                if self.mapa[i][j] == 91:

                    m = suelo(self.sabana[0][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                #Pinta los fondos
                """if self.mapa[i][j] == 92:

                    m = suelo(self.sabana[1][9])
                    m.setpos(j*40 , i*40)
                    self.fondos.add(m)
                    self.general.add(m)"""

                #pinta lava en el tercermundo
                if self.mapa[i][j] == 93:

                    m = lava(j*40 , i*40)
                    #m.setPos(j*40 , i*40)
                    #self.fondos.add(m)
                    self.general.add(m)


                #Base del tercer mundo
                if self.mapa[i][j] == 94:

                    m = suelo(self.sabana[3][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 95:

                    m = suelo(self.sabana[4][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 96:

                    m = suelo(self.sabana[5][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 97:

                    m = suelo(self.sabana[6][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 98:

                    m = suelo(self.sabana[7][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 99:

                    m = suelo(self.sabana[8][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)
