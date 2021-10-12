import os
import array
import sys

def max_heapify(a,n,i):
    left=2*i
    right=2*i+1
    if left<= n-1 and a[left] > a[i]:
        maximum=left
    else: maximum=i

    if right<=n-1 and a[right]>a[maximum]:
        maximum=right
    if maximum !=i:
        a[i],a[maximum]=a[maximum],a[i]
        max_heapify(a,n,maximum)

def heap_sort(a):
    n=build_max_heap(a)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        n-=1
        max_heapify(a,i,0)
    return a

def build_max_heap(a):
    n=len(a)
    for i in range(n//2-1,-1,-1):
        max_heapify(a,n,i)
    return n
