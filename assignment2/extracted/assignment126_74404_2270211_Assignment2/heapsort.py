from buildmaxheap import buildmaxheap
from maxheap import maxheap
def heapsort(arr):
    length = len(arr);
    a = buildmaxheap(arr,length);
    heapsize = len(arr);
    for i in range (heapsize-1,-1,-1):   #start in one or two, try
        #print("in)")
        swap(arr,0,i);
        maxheap(arr,0,i)



def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t
