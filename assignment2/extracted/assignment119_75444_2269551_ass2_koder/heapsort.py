def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

#Heap = ordnat binart trad

def build_max_heap(A):  
    heapsize = len(A)
    for i in range(heapsize//2-1,-1,-1):
        max_heapify(A,heapsize,i)
    

def max_heapify(A,heapsize,i):     #Lik BMH men antar att en del av listan redan ar sorterad
    I = 2*i+1         #Tar hogsta nummret langst upp i trader och byter me lagsta
    r = 2*i+2
    if I < heapsize and A[I]>A[i]:
        largest = I
    else:
        largest = i
    if r < heapsize:
        if(A[r]>A[largest]):
            largest = r
    if largest != i:
        swap(A,i,largest)
        max_heapify(A,heapsize,largest)

        
def heap_sort(A):
    heapsize = len(A)
    build_max_heap(A)
    for i in range(heapsize-1,0,-1):
        swap(A,0,i)
        heapsize = heapsize-1
        max_heapify(A,heapsize,0)


