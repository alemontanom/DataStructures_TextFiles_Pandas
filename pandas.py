#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:16:05 2021

@author: alemontano
"""
import pandas as pd

"""cargar archivos :
    archivo=pd.read_txt("nombre.txt", index_col=0 (cual columna quieres que tome como indice), 
    usecols=[0,1] (si quieres deshacerte de algunas columnas), 
    skiprows=1 (cuenta de arriba a abajo), 
    skipfooter=1 (cuenta de abajo a arriba), 
    header=None) #el header es si no tienen nombre las columnas en el archivo
    
    
    archivo.columns para asignar nombre a las columnas 
"""
datos = {"nombre": ("Anastacia", "Dima", "Katherine", "James", "Emily", "Michael", "Matthew", "Laura", "Kevin", "Jonas"), 
         "puntaje": (12.5, 9, 16.5, 0, 9, 20, 14.5, 0, 8, 9), 
         "intentos": (1, 3, 2, 3, 2, 3, 1, 1, 2, 1),
         "califica": ("si", "no", "si", "no", "no", "si", "si", "no", "no", "no")}

indice = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k"]

#crear transpuesta
df = pd.DataFrame(datos, index=indice)
print(df)

#obtener transpuesta
print(df.T) 

#Obten informacion de datos estadísticos descriptivos 

print(df.describe())

#informacion estructural 
print(df.info())

#numero de renglones
print(df.shape[0]) #.shape imprime (renglones, columnas)

#los primeros tres renglones
print(df[:3]) #[0:3]
print(df[:"c"]) #[a:c]
print(df.iloc[[0, 1, 2]]) #iloc[0:3], .loc[:"c"]

#ultimos tres renglones 
print(df[-3:])

#ordena por puntaje
print(df.sort_values("puntaje", ascending = False ))

#ordena por puntajes e intentos
print(df.sort_values(by=["puntaje", "intentos"], ascending=[False, True]))

#Obten columna nombre e intentos 
print(df[["nombre", "intentos"]])

#filtros: renglones con intentos mayor o igual a 2
print(df[df["intentos"] >= 2])

#renglones con puntaje entre 15 y 20
print(df[(df["puntaje"]<=20) & (df["puntaje"]>=15)])

#intentos menores a 3 y puntaje mayor a 15
print(df[(df["intentos"]<3) & (df["puntaje"]>=15)])  #para or usas |

#actualiza el puntaje del renglon h y d 
df.loc["h","puntaje"]=10 
df.loc["d","puntaje"]=10 
df.loc[["h", "d"], "puntaje"]=[10, 11] 

#suma y promedio de intentos 
print(df["intentos"].sum())
print(df["intentos"].mean())

#quita el renglon i 
df=df.drop("i")

#quitar columna intentos
df = df.drop("intentos", axis=1)

#agrega nuevo participante 
serie = pd.Series({"nombre": "Octavio", "puntaje": 25, "califica": "si"}, name="l")

df = df.append(serie)

#info de nombre y puntaje de d, c y a
print(df.loc[["d", "c", "a"], ["nombre", "puntaje"]])