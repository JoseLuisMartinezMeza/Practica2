# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:50:10 2023

@author: El Pepe
"""
import random

#Se importa el módulo random para generar números aleatorios.
def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    else:
        # Elegimos un pivote
        pivote = arreglo[0]
        # Creamos dos arreglos: una con los elementos menores que el pivote y otra con los elementos mayores que el pivote
        menores = [x for x in arreglo[1:] if x < pivote]
        mayores = [x for x in arreglo[1:] if x >= pivote]
        # Ordenamos recursivamente las dos arreglos y concatenamos el resultado
        return quicksort(menores) + [pivote] + quicksort(mayores)
    
    
arreglo = [random.randint(1, 100) for _ in range(5)]
print("arreglo original:", arreglo)
arreglo_ordenado = quicksort(arreglo)
print("arreglo ordenado:", arreglo_ordenado)