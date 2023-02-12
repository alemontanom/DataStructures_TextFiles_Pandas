#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 16:18:33 2021

@author: alemontano
"""

with open("itam.txt", encoding="utf-8") as archivo:
    texto = archivo.read()

texto = texto.upper() #facilita la identificacion de caracteres iguales     
letrasAcentos = ("Á", "É", "Í", "Ó", "Ú")
vocales = ("A", "E", "I", "O", "U")

for elemento in zip(letrasAcentos, vocales):
    texto = texto.replace(elemento[0], elemento[1])
    #nos quita los acentos 
    
basuras = (";", ":", ",", ".", "-", "0", "1", "2", "3", 
           "4", "5", "6", "7", "8", "9", "«", "»")

for basura in basuras:
    texto = texto.replace(basura, "")
    #quita todos los caracteres en la tupla basura del texto
    
otros = (" Y ", " DEL ", " DE ", " EL ", " LA ", " AL ", " LOS ", " LAS ", " LES ", " E ")

for otro in otros:
    texto = texto.replace(otro, " ")  

palabras = {}

lista = texto.split()

for palabra in lista:
    if palabra in palabras:
        palabras[palabra] += 1 
    else:
        palabras[palabra] = 1

palabras = list(palabras.items())

palabras.sort(key = lambda p : p[1])

print(palabras)



