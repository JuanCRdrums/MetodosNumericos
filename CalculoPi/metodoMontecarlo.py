#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random
import time

#---------------------MÉTODO MONTECARLO---------------------------
#Complejidad n²

n = 1000000 #cantidad de puntos aleatorios																																																																																																																																																																																	 #cantidad de valores aleatorios para x e y
d = float(4) #diámetro de la circunferencia
r = d / 2 #radio de la circunferencia
a = d*d #área del cuadrado
puntos = [] #coordenadas de los puntos generados 

dentro = float(0) #puntos dentro de la circunferencia
fuera = float(0) #puntos por fuera de la circunferencia
inicio = time.clock()

for i in range(n):#se generan números aleatorios para x e y en el rango entre -r y r
	x = random.uniform(-r,r)
	y = random.uniform(-r,r)
	puntos.append((x,y))
	if puntos[i][0]*puntos[i][0] + puntos[i][1]*puntos[i][1] <= r*r: # x² + y² <= r² (está dentro de la circunferencia)
		dentro += 1
	else:
		fuera += 1

final = time.clock()
demora = final - inicio
piMontecarlo = (a*dentro)/(float(n)*r*r) #ecuación para calcular pi a través del Método Montecarlo
error = abs(piMontecarlo*100/math.pi - 100)
print "\tAPROXIMACIÓN DE PI POR MÉTODOS NUMÉRICOS"
print "----------------------------------------------------------"
print "Método Montecarlo:"
print "Radio de la circunferencia: ",r
print "Cantidad de puntos: ",n
print "Valor de pi calculado: ", piMontecarlo
print "Porcentaje de error: ", error
print "Cantidad de iteraciones: ",i
print "Tiempo de ejecución: ",demora




