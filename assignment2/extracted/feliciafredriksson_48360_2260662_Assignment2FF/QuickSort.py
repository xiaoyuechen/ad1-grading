# -*- coding: utf-8 -*-
"""
Felicia Fredriksson
Algorithms and datastructure 1
Assignment 2


Implimentation of:
QuickSort()
"""

def Partition(A,p,r):
    q = A[r] #Pick pivot element as last element in A.
    i = p-1 #Pointer to last element in left subarray, i.e elements < q
    for j in range(p,r):
        if A[j] <= q:
            i = i+1 #Step forward with pointer
            A[i], A[j] = A[j], A[i] #Swap value at j and i
    
    #Swap q to right place
    A[i+1], A[r] = A[r], A[i+1]
    return i+1 #Return the position of q, pivot element
            

"""Use Partition to implement QuickSort
Conqure and Merge step in algorithm
"""
def QuickSort(Q, l, h):
    if len(Q) == 1: #Length one and thus already sorted
        return Q
    if l < h:
        q = Partition(Q,l,h)
        #Recursive call for each subarray on both sides of pivot element
        QuickSort(Q, l, q-1)
        QuickSort(Q, q+1,h) 
        #In place operations, no return needed