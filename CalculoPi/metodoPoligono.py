#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random

#------------MÉTODO DEL POLÍGONO----------------

#Complejidad computacional: log2(l)


l = 10000 #cantidad máxima de lados para el polígono a usar. Se calculará hasta la potencia de 2 inmediatamente anterior

i = 4 #iterador para la cantidad de lados que se calculan
d = math.sqrt(2) #medida de un cuadrado inscrito dentro de una circunferencia de radio 1

while i <= l:
	if l >= 4 and l < 8: #para el caso en el que sea un cuadrado
		lado = d
		pi = (i*lado)/2
	else:
		lado = math.sqrt(2-2*math.sqrt(1 - (d**2)/4))
	n = i*2 #cantidad de lados del polígono actual
	pi = (n*lado)/2
	i = i*2 #se duplica la cantidad de lados del polígono
	d = lado

error = abs(pi*100/math.pi - 100)


print "\t MÉTODO DEL POLÍGONO"
print "Cantidad de lados del polígono: ",i/2
print "Valor de pi calculado: ",pi
print "Porcentaje de error: ",error
