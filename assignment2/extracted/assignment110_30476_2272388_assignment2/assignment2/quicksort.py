#!/usr/bin/env python
# encoding: utf-8

def swap1(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def Partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            swap1(a, i, j)
    swap1(a, i+1, r)
    return i+1

def quicksort(a, p, r):
    if p <= r:
        q = Partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)

