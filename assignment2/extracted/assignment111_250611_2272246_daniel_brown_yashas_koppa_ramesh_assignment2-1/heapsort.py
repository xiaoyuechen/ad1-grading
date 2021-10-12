#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insertion sort implementation. Sorts an array A in place.
"""

def Max_Heapify(a,size,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and a[left] > a[i]:
        largest = left
    if right < size and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]  # Swapping largest with parent node
        Max_Heapify(a, size, largest)
def heapsort(a, size):
    for i in range(size//2, -1, -1):
        Max_Heapify(a, size,i)

    for i in range(size-1, -1, -1):
        a[i], a[0] = a[0], a[i]  # Swapping root with last element
        Max_Heapify(a, i, 0)









