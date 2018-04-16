#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random
import time

#-----------------SERIE DE LEIBNIZ-------------------
#Complejidad lineal


n = 30000000 #cantidad de iteraciones deseada
serie = 0.0
inicio = time.clock()
for i in range(n):
	num = float((-1)**i)
	den = float(2*i + 1)
	serie = serie + num/den
	
final = time.clock()
demora = final - inicio
pi = 4*serie
error = abs(pi*100/math.pi - 100)

print "\t Cálculo de PI con la serie de Leibniz"
print "Valor de pi calculado: ",pi
print "Porcentaje de error: ",error
print "Cantidad de iteraciones: ",i
print "Tiempo de ejecución: ",demora