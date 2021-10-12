#!/usr/bin/env python
# encoding: utf-8

def swap2(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def max_heapify(a, i, a_heap_size):
    l = i*2
    r = i*2+1
    if l < a_heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < a_heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap2(a, i, largest)
        max_heapify(a, largest, a_heap_size)


def build_max_heap(a):
    for i in range(int(len(a)/2-1), -1, -1):
        max_heapify(a, i, len(a))

def heapsort(a):
    build_max_heap(a)
    a_heap_size = len(a)
    for i in range(a_heap_size-1, 0, -1):
        swap2(a, 0, i)
        a_heap_size -= 1
        max_heapify(a, 0, a_heap_size-1)
