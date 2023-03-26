# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 21:34:15 2023

@author: El Pepe
"""

import random
#Se importa el módulo random para generar números aleatorios.
def ordenamiento_por_insercion(arreglo):
     # Contamos cuántos elementos son más pequeños que el elemento actual
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i-1
        while j >=0 and clave < arreglo[j] :
            # Colocamos el elemento en su posición adecuada
                arreglo[j+1] = arreglo[j]
                j -= 1
        arreglo[j+1] = clave
    return arreglo

arreglo = [random.randint(1, 1000) for _ in range(5)]
print("arregloeglo original:", arreglo)
arreglo_ordenado = ordenamiento_por_insercion(arreglo)
print("arregloeglo ordenado:", arreglo_ordenado)
