#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:11:31 2021

@author: alemontano
"""

estados = []
datos = []
encabezado = ""
with open("datos.txt", "r", encoding="utf-8") as archivo: #se usaria otro archivo para no modificar los datos originales
    lineas = archivo.readlines()
    encabezado = lineas[0].strip()
    pie = lineas[-1]
    lineas = lineas[1:len(lineas)-1]
    for linea in lineas:
        linea = linea.strip().split(",")
        estados.append(linea[0])
        linea = linea[1:len(linea)]
        estado = [] 
        estado = list(map(float, linea))
        datos.append(estado)


i=0

with open("procesado.csv", "w") as archivo:
    archivo.write(encabezado+","+"Desconocido\n")
    while i < len(estados):
        linea = estados[i]+":\n"
        # linea += ",".join(list(map(str,datos[i])))+"," en vez del for
        for dato in datos[i]:
            linea += str(dato) + ", "
        linea += str(100 - (datos[i][-1]+datos[i][-2]))
        archivo.write(linea + "\n")
        i += 1
    archivo.write(pie)
    
union = ","
print(union.join(list(map(str, [1, 2, 3]))))

    

