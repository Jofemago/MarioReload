import pygame
from Enemys import *
from configuraciones import *


class MakeEnemys:

    def __init__(self,mapa ,sabana, enemigosa, enemigosb, suelos, general):

        self.mapa = mapa
        #print mapa
        self.sabana = sabana
        self.EnemigosA = enemigosa
        self.EnemigosB = enemigosb
        self.suelos = suelos
        self.general = general
        self.filas = len(self.mapa)
        self.col = len(self.mapa[0])


        #self.nivel = nivel
        #print self.filas, self.col

    def dibujarmapa(self):

        for i in range(self.filas):
            for j in range(self.col):
                #se dibujan suelos
                if self.mapa[i][j] == 21:
                    #print 'Goomba creado'
                    m = Goomba(j*40 , i*40,'Jugadores/Enemigos/imgenemigos/Goomba1.png',self.suelos)

                    self.EnemigosA.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 61:
                    #print 'Goomba creado'
                    m = Goomba(j*40 , i*40,'Jugadores/Enemigos/imgenemigos/Goomba2.png',self.suelos)

                    self.EnemigosA.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 62:
                    #print 'Goomba creado'
                    m = Goomba(j*40 , i*40,'Jugadores/Enemigos/imgenemigos/boo.png',self.suelos)

                    self.EnemigosA.add(m)
                    self.general.add(m)


                if self.mapa[i][j] == 15: #planta Carnivora
                    m = Carnivora(j*40 , i*40,'Jugadores/Enemigos/imgenemigos/carnivora.png')

                    self.EnemigosB.add(m)
                    self.general.add(m)
