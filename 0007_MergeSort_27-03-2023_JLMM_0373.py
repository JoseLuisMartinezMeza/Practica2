# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:02:14 2023

@author: El Pepe
"""

import random

def mergeSort(arreglo):
    # Si la longitud de la lista es mayor que 1
    if len(arreglo) > 1:
        # Encuentra el punto medio de la lista
        mid = len(arreglo)//2
        # Divide la lista en dos mitades
        L = arreglo[:mid]
        R = arreglo[mid:]

        # Llama recursivamente a mergeSort en ambas mitades
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copia los datos a las listas temporales L[] y R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arreglo[k] = L[i]
                i += 1
            else:
                arreglo[k] = R[j]
                j += 1
            k += 1

        # Verifica si quedan elementos en alguna de las listas
        while i < len(L):
            arreglo[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arreglo[k] = R[j]
            j += 1
            k += 1

# Genera una lista de 5 números aleatorios del 1 al 100
arreglo = random.sample(range(1, 101), 5)
print("Lista original:", arreglo)
mergeSort(arreglo)
print("Lista ordenada:", arreglo)