# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:49:17 2023

@author: El Pepe
"""

import random

def natural_merge_sort(arreglo):
    # Función para dividir la arreglo en sub-arreglos ordenadas
    def split_runs(arreglo):
        runs = []
        current_run = [arreglo[0]]
        for i in range(1, len(arreglo)):
            if arreglo[i] >= current_run[-1]:
                current_run.append(arreglo[i])
            else:
                runs.append(current_run)
                current_run = [arreglo[i]]
        runs.append(current_run)
        return runs

    # Función para combinar dos sub-arreglos ordenadas en una sola arreglo ordenada
    def merge(l1, l2):
        result = []
        i = j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        result.extend(l1[i:])
        result.extend(l2[j:])
        return result

    # Dividir la arreglo en sub-arreglos ordenadas
    runs = split_runs(arreglo)
    # Combinar las sub-arreglos hasta que quede una sola arreglo ordenada
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i == len(runs) - 1:
                new_runs.append(runs[i])
            else:
                new_runs.append(merge(runs[i], runs[i+1]))
        runs = new_runs
    return runs[0]

# Genera una arreglo de 5 números aleatorios del 1 al 100
arreglo = random.sample(range(1, 101), 5)
print("arreglo original:", arreglo)
arreglo = natural_merge_sort(arreglo)
print("arreglo ordenada:", arreglo)