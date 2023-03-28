# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:27:39 2023

@author: El Pepe
"""

import random

def merge(arreglo, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arreglo[p + i]
    for j in range(0 , n2):
        R[j] = arreglo[q + j + 1]
    i = 0
    j = 0
    k = p
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arreglo[k] = L[i]
            i += 1
        else:
            arreglo[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arreglo[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arreglo[k] = R[j]
        j += 1
        k += 1

def mergeSort(arreglo,p,r):
    if p < r:
        q = (p+(r-1))//2
        mergeSort(arreglo, p, q)
        mergeSort(arreglo, q+1, r)
        merge(arreglo, p, q, r)

# Genera una arreglo de 5 números aleatorios del 1 al 100
arreglo = random.sample(range(1, 101), 5)
n = len(arreglo)
print("arreglo original:", arreglo)
mergeSort(arreglo,0,n-1)
print("arreglo ordenada:", arreglo)