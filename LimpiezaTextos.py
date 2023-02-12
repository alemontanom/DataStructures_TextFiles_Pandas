#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:21:34 2021

@author: alemontano
"""

def limpiar(nombres) : 
    #estandarizar en buen formato los nombres dados
    reemplazar = ["0", "1", "3"]
    corregir = ["O", "I", "E"]
    indeseables = [".", ",", ";", ":"]
    for i in range(len(nombres)) :
        nombres[i] = nombres[i].upper().strip()
        for k in range(len(indeseables)):
            nombres[i] = nombres[i].replace(indeseables[k], "")
        for j in range(len(reemplazar)) : 
            nombres[i] = nombres[i].replace(reemplazar[j], corregir[j])
    
    return nombres; 
            

n = int(input("Cuántos nombres quiere ingresar? : "))
nombres = []

for i in range(n):
    nombres.append(input("Ingresa el nombre "+ str(i+1)+ ": ")) 

print(limpiar(nombres))
    