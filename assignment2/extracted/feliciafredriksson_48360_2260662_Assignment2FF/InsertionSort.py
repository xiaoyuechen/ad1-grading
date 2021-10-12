# -*- coding: utf-8 -*-
"""
Felicia Fredriksson
Algorithms and datastructure 1
Assignment 2

Implimentation of:
InserionSort()

"""

def InsertionSort(A):
    for j in range(1,len(A)):
        key = A[j] #Store value for swap
        i = j-1 #First value in sorted subarray
        while i>=0 and A[i] > key:
            A[i+1] = A[i] #"Overwright" the value one step to the right
            i = i-1 
        A[i+1] = key #Place key at its new position


