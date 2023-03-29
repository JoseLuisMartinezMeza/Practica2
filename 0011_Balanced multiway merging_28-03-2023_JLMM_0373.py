# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:34:59 2023

@author: El Pepe
"""

import random

# Generamos una arreglo de 5 números aleatorios del 1 al 100
numeros = [random.randint(1, 100) for _ in range(5)]

# Función para dividir la arreglo en subarreglos
def dividir_arreglo(arreglo):
    # Calculamos el tamaño de las subarreglos
    tamano_subarreglo = len(arreglo) // 2
    # Dividimos la arreglo en dos subarreglos
    subarreglo_izquierda = arreglo[:tamano_subarreglo]
    subarreglo_derecha = arreglo[tamano_subarreglo:]
    return subarreglo_izquierda, subarreglo_derecha

# Función para mezclar dos subarreglos ordenadas
def mezclar_subarreglos(subarreglo_izquierda, subarreglo_derecha):
    # Creamos una arreglo vacía para almacenar el resultado
    resultado = []
    # Mientras ambas subarreglos tengan elementos
    while subarreglo_izquierda and subarreglo_derecha:
        # Comparamos el primer elemento de cada subarreglo
        if subarreglo_izquierda[0] < subarreglo_derecha[0]:
            # Si el primer elemento de la subarreglo izquierda es menor,
            # lo añadimos al resultado y lo eliminamos de la subarreglo izquierda
            resultado.append(subarreglo_izquierda.pop(0))
        else:
            # Si el primer elemento de la subarreglo derecha es menor o igual,
            # lo añadimos al resultado y lo eliminamos de la subarreglo derecha
            resultado.append(subarreglo_derecha.pop(0))
    # Si alguna de las subarreglos todavía tiene elementos, los añadimos al resultado
    resultado.extend(subarreglo_izquierda)
    resultado.extend(subarreglo_derecha)
    return resultado

# Función para realizar el ordenamiento Balanced multiway merging
def balanced_multiway_merging(arreglo):
    # Si la arreglo tiene menos de 2 elementos, ya está ordenada
    if len(arreglo) < 2:
        return arreglo
    # Dividimos la arreglo en dos subarreglos
    subarreglo_izquierda, subarreglo_derecha = dividir_arreglo(arreglo)
    # Ordenamos cada subarreglo recursivamente
    subarreglo_izquierda = balanced_multiway_merging(subarreglo_izquierda)
    subarreglo_derecha = balanced_multiway_merging(subarreglo_derecha)
    # Mezclamos las subarreglos ordenadas
    return mezclar_subarreglos(subarreglo_izquierda, subarreglo_derecha)

# Ordenamos la arreglo utilizando Balanced multiway merging
numeros_ordenados = balanced_multiway_merging(numeros)

# Mostramos el resultado
print(numeros_ordenados)