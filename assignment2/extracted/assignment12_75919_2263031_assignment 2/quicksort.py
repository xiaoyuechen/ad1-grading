import os
import array
import sys
#Quicksort Implementation
def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t
    
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r): 
        if A[j]<=x:
            i=i+1
            swap(A,i,j)
    swap(A,i+1,r)
    return i+1
        
    
def quicksort(a,p,r):
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
    
    


def run_quicksort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing quicksort
    # Call your quicksort implementation here
    quicksort(a,0,len(a)-1)

    # output nums_sorted.txt
    nums_sorted = open('quicksorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

    
