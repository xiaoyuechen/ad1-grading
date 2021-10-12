

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def heapSort(a):
    buildMaxHeap(a)
    heapsize = len(a)-1
    for i in range(heapsize,0,-1):
        swap(a,0,i)
        heapsize = heapsize-1
        maxHeapify(a,0,heapsize)

def buildMaxHeap(a):
    for i in range(int(len(a)/2),-1,-1):
        maxHeapify(a,i,len(a)-1)

def maxHeapify(a,i,length):
    l = 2*i+1
    r = 2*i+2
    
    if l <= length and a[l]>a[i]:
        largest = l
    else: 
        largest = i
    if r<= length:
        if a[r]>a[largest]:
            largest = r
    if largest != i:
        swap(a,i,largest)
        maxHeapify(a,largest,length)


