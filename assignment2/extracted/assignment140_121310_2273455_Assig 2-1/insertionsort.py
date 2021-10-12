# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:32:30 2021

@author: andre
"""
lista = [5,4,6,3,2,1]

def insertionsort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i-1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j = j-1
        x[j+1] = key
    return x

print(lista)
print(insertionsort(lista))

L = insertionsort(lista)

f = open("insertionsorted.txt", "w+")
for i in L:
    f.writelines("%s\n" % i)
f.close()