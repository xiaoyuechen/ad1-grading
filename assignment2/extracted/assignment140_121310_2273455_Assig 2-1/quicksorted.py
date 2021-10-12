# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:01:38 2021

@author: andre
"""
lista = [4,6,2,3,1,8,7,9,5]
#print(lista)



def partition(A, p, r):
     x = A[r]
     i = p-1
     for j in range(p, r-1):
         if A[j] <= x:
             i += 1
             A[j], A[i] = A[i], A[j]
     A[i+1], A[r] = A[r], A[i+1]
     #return i + 1, A
     return i+1


def quicksort(A, p, r):
    if len(A) == 1:
        return A
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A


#print(partition(lista,1, len(lista)-1))
n = len(lista)

#print(partition(lista,1, len(lista)-1))

L = quicksort(lista, 0, n-1)

f = open("quicksorted.txt", "w+")
for i in L:
    f.writelines("%s\n" % i)
f.close()

