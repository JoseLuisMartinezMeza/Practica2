# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:35:54 2023

@author: El Pepe
"""

import random

def ordenamiento_por_burbuja(arreglo):
    n1 = len(arreglo)
    for i in range(n1):
        for j in range(0, n1-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    return arreglo

arreglo = [random.randint(0, 100) for _ in range(10)]
print("Arreglo original:", arreglo)
arreglo_ordenado = ordenamiento_por_burbuja(arreglo)
print("Arreglo ordenado:", arreglo_ordenado)