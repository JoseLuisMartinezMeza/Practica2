# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:50:35 2023

@author: El Pepe
"""
import random

def seleccion_directa(arreglo):
    # Recorremos todo el arreglo excepto el último elemento
    for i in range(len(arreglo)-1):
        # Encontramos el valor mínimo en la arreglo restante
        minimo = i
        for j in range(i+1, len(arreglo)):
            if arreglo[j] < arreglo[minimo]:
                minimo = j
        # Intercambiamos el valor mínimo con el primer elemento del arreglo restante
        arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]
    return arreglo


arreglo = [random.randint(1, 100) for _ in range(5)]
print("arreglo original:", arreglo)
arreglo_ordenado = seleccion_directa(arreglo)
print("arreglo ordenado:", arreglo_ordenado)