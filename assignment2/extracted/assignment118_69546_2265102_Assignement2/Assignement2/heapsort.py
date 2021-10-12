def maxheapify(A,i,heapsize):
    l=2*i+1
    r=2*i+2
    if l<heapsize and A[l]>A[i]:
        largest=l
    else:
        largest=i
            
    if r<heapsize and A[r]>A[largest]:
        largest=r
    if largest !=i:
        temp=A[i]
        A[i]=A[largest]
        A[largest]=temp
        maxheapify(A,largest,heapsize)

def buildmaxheap(A,heapsize):
    for i in range(int(heapsize/2)-1,-1,-1):
        maxheapify(A,i,heapsize)
        

def heapsort(A):
    heapsize=len(A)
    buildmaxheap(A,heapsize)
    for i in range(len(A)-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapsize-=1
        maxheapify(A,0,heapsize)
