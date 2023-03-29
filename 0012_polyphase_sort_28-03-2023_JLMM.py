# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:54:06 2023

@author: El Pepe
"""
import random
def polyphase_sort(arr):
    block_size = 2
    num_blocks = (len(arr) + 1) // block_size
    buffer = [0] * (num_blocks * block_size)

    buffer[:len(arr)] = arr[:]

   
    for i in range(0, num_blocks, 2):
        left = i * block_size
        right = (i + 1) * block_size
        buffer[left:right] = sorted(buffer[left:right])

  
    while num_blocks > 1:
        blocks = [buffer[i*block_size:(i+1)*block_size] for i in range(num_blocks)]
        merged_blocks = []
        for i in range(0, num_blocks, 2):
            left = blocks[i]
            right = blocks[i+1] if i+1 < num_blocks else None
            merged = merge_blocks(left, right)
            merged_blocks.extend(merged)

        buffer[:len(merged_blocks)] = merged_blocks[:]
        num_blocks = (num_blocks + 1) // 2

    return buffer

def merge_blocks(left, right):
    if right is None:
        return left

    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
arreglo = random.sample(range(1, 100), 5)
print("arreglo original:", arreglo)
arreglo = polyphase_sort(arreglo)
print("arreglo ordenada:", arreglo)
print()