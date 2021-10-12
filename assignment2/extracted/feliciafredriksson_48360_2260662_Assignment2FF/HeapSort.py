# -*- coding: utf-8 -*-
"""
Felicia Fredriksson
Algorithms and datastructure 1
Assignment 2

Implimentation of:
HeapSort()
"""

def MaxHeapify(A,n,i):
    #Takes an array and index i, assume subtrees with root i are maxheaps
    #n is size of A
    left = 2*i+1 #Need to add 1 and 2 here due to array index in python starts at 0
    right = 2*i+2 
    bigger = i 
    if left < n and A[left] > A[bigger]: #Check left child
        bigger = left
    if right < n and A[right] > A[bigger] : #Check right child
        bigger = right
    if bigger != i: #Then we need to swap to get a max-heap
        A[i], A[bigger] = A[bigger], A[i] #Swap
        MaxHeapify(A, n, bigger) #Go down one branch



def BuildMaxHeap(A):
   #Construct a MaxHeap of A. We use MaxHeapify in "revers" from bottom up.
   size = len(A)
   for i in range(size//2-1, -1, -1): #len(A)//2-1 is first index that is not a leaf
       MaxHeapify(A,size,i)


def HeapSort(A):
    BuildMaxHeap(A)
    heapsize = len(A)-1 #Intial heap-size, minus one since index 0 is first
    while heapsize >= 1:
        A[0], A[heapsize] = A[heapsize], A[0] #Swap root with right-most leaf
        heapsize = heapsize - 1 #Discard that leaf (Already sorted)
        MaxHeapify(A, heapsize,0) #Restore max-heap from root, i = 0, with shorter heap size
        
        