import os
import array
import sys
import math
#Heapsort Implementation
def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t
def maxheapify(A,heapsize,i):
    l=2*i+1   #left(i)
    r=2*i+2  #right(i)
    if l<=heapsize and A[l]>A[i]:
        largest=l   
    else:
        largest=i    
    if r<=heapsize and A[r]>A[largest]:
        largest=r   
    if largest != i:
        swap(A,i,largest)
        maxheapify(A,heapsize,largest)
        
 
def buildmaxheap(A):
    heapsize=len(A)-1
    for i in range((len(A)-1)//2,-1,-1):
        maxheapify(A,heapsize,i)
        

def heapsort(A):
    buildmaxheap(A)
    heapsize=len(A)-1
    for i in range(len(A)-1,0,-1):    
        swap(A,0,i)
        heapsize=heapsize-1
        maxheapify(A,heapsize,0)


def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
    heapsort(a)

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()
