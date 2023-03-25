# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:34:15 2023

@author: El Pepe
"""

import random

def ordenamiento_por_insercion(arreglo):
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i-1
        while j >=0 and clave < arreglo[j] :
                arreglo[j+1] = arreglo[j]
                j -= 1
        arreglo[j+1] = clave
    return arreglo

arreglo = [random.randint(1, 1000) for _ in range(5)]
print("arregloeglo original:", arreglo)
arreglo_ordenado = ordenamiento_por_insercion(arreglo)
print("arregloeglo ordenado:", arreglo_ordenado)