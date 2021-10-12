import os
import array
import sys

def partition(a,p,r):

    x=a[r]
    i=p-1
    
    #print(i)
    
    for j in range(p,r):
            if a[j]<=x:
                #print('hej')
                i+=1
                a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return(i+1)

def quicksort(a,p,r):
    if len(a)==1:
        return a
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
