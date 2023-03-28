# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:15:39 2023

@author: El Pepe
"""

import random

# Función para hacer el conteo de ordenamiento de arreglo[] de acuerdo a
# el dígito representado por exp.
def countingSort(arreglo, exp1):
    n = len(arreglo)
    # La matriz de salida que tendrá los números ordenados
    output = [0] * (n)
    # Inicializar el conteo de la matriz
    count = [0] * (10)
    # Almacena el conteo de ocurrencias en count[]
    for i in range(0, n):
        index = (arreglo[i] // exp1)
        count[(index) % 10] += 1
    # Cambia count[i] para que count[i] ahora contenga la posición real
    # de este dígito en la salida[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Construye la matriz de salida
    i = n - 1
    while i >= 0:
        index = (arreglo[i] // exp1)
        output[count[(index) % 10] - 1] = arreglo[i]
        count[(index) % 10] -= 1
        i -= 1
    # Copia la matriz de salida a arreglo[], para que arreglo[] ahora contenga
    # números ordenados de acuerdo al dígito actual
    i = 0
    for i in range(0, len(arreglo)):
        arreglo[i] = output[i]

# Método para hacer Radix Sort
def radixSort(arreglo):
    # Encuentra el número máximo para conocer el número de dígitos
    max1 = max(arreglo)
    # Hacer el conteo de ordenamiento para cada dígito. En lugar de pasar el número de dígitos,
    # exp se pasa. exp es 10^i donde i es el dígito actual
    exp = 1
    while max1 // exp > 0:
        countingSort(arreglo, exp)
        exp *= 10

# Genera una arregloeglo de 5 números aleatorios del 1 al 100
arreglo = random.sample(range(1, 101), 5)

print("arreglo original:", arreglo)
radixSort(arreglo)
print("arreglo ordenada:", arreglo)
