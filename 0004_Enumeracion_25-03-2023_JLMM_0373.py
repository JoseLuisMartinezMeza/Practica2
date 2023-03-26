# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:09:35 2023

@author: El Pepe
"""
import random


def Algoritmos_de_enumeracion(arreglo):
    n = len(arreglo)
    resultado = [0] * n
    for i in range(n):
        # Contamos cuántos elementos son más pequeños que el elemento actual
        conteo = 0
        for j in range(n):
            if arreglo[j] < arreglo[i]:
                conteo += 1
        # Colocamos el elemento en su posición adecuada
        resultado[conteo] = arreglo[i]
    return resultado

arreglo = [random.randint(1, 100) for _ in range(5)]
print("arreglo original:", arreglo)
arreglo_ordenado = Algoritmos_de_enumeracion(arreglo)
print("arreglo ordenado:", arreglo_ordenado)