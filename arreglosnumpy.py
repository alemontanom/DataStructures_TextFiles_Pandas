#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:11:08 2021

@author: alemontano
"""

import numpy as np 

arreglo = np.array([101, 102, 103, 104, 105])#se le puede especificar el dtype para que use menos espacio, ej dtype=i2 dice que solo quite el espacio de dos bytes por elemento en el arreglo

#arreglo = arreglo.astype("i2") reduce/aumenta el tamaño que ocupa el arreglo

arreglo = np.append(arreglo, 201)

print(np.insert(arreglo, 1, 500)) #no lo modifica si no añades el =, solo te regresa un arreglo con eso

print(np.delete(arreglo, 2)) # borra el del indice 1

print(arreglo * arreglo)

arreglo = arreglo + 1 


print(arreglo, arreglo.itemsize, arreglo.size, arreglo.shape, arreglo.dtype) 

print(arreglo[arreglo < 105])



mod = arreglo * 6
mod[arreglo < 105] = mod[arreglo < 105] * 12 #solo modifica los que cumples con la condicion del lado izquierdo del igual 

filtro_reduccion = arreglo > 105 

mod[filtro_reduccion] = mod[filtro_reduccion] * 0.5

matriz = np.array([[102, 3],
                  [200, 46],
                  [150, 53]])

print(matriz.transpose()) 

print(matriz.mean(axis=0)) #min, max, argmin=posicion del minimo (indice), std, np.median(arreglo) 

print(matriz.mean(axis=1))