def maxheapify(A,n,i):
    l=2*i+1
    r=2*i+2
    largest=i
    if l < n and  A[l] > A[i]:
        largest = l

    if r < n and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i],A[largest] = A[largest], A[i]
        maxheapify(A,n,largest)

def buildmaxheap(A,n):
    for i in range(n//2,-1,-1):
        maxheapify(A,n,i)

def heapSort(A):
    n=len(A)
    buildmaxheap(A,n)
    for i in range(n-1,0, -1):
        A[i],A[0] = A[0], A[i]
        maxheapify(A,i,0)
