# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:31:21 2023

@author: El Pepe
"""



import random
#Se importa el módulo random para generar números aleatorios.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
#Se define una clase Nodo que representa un nodo en un árbol binario. 
#Cada nodo tiene un valor y dos hijos: izquierda y derecha.

def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.valor < nodo.valor:
            if raiz.derecha is None:
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)
#Se define una función insertar que inserta un nodo en el árbol binario. Si la raíz es None, 
#se asigna el nodo como raíz. Si el valor del nodo es mayor que el valor de la raíz, 
#se inserta en el subárbol derecho. Si el valor del nodo es menor o igual que el valor de la raíz, 
#se inserta en el subárbol izquierdo.

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.valor)
        inorden(raiz.derecha)
#Se define una función inorden que recorre el árbol binario en orden (izquierda, raíz, derecha) 
#e imprime los valores de los nodos.

def ordenamiento_de_arbol(arreglo):
    raiz = Nodo(arreglo[0])
    for i in range(1, len(arreglo)):
        insertar(raiz, Nodo(arreglo[i]))
    inorden(raiz)
#Se define una función ordenamiento_de_arbol que toma un arreglo como entrada y 
#lo ordena utilizando un árbol binario. Primero se crea la raíz del árbol con el 
#primer elemento del arreglo. Luego se insertan los demás elementos en el árbol utilizando 
#la función insertar. Finalmente se recorre el árbol en orden utilizando la función inorden.

arreglo = [random.randint(0, 100) for _ in range(10)]
print("arregloeglo original:", arreglo)
arreglo_ordenado = ordenamiento_de_arbol(arreglo)
