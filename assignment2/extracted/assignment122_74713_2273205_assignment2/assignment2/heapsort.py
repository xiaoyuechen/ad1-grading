from math import floor
heapsize=None
def right(i):
    return 2*(i)+2
def left(i):
    return 2*i+1

def build_max_heap(A):
    for i in range (floor(len(A)/2),-1,-1):
        max_heapify(A,i)
    return A

def max_heapify(A,i):
    global heapsize
    l = left(i)
    r = right(i)
    if l <= heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if (r <= heapsize) and A[r] > A[largest]:
        largest = r
    if largest!=i:
        temp = A[i]
        A[i]=A[largest]
        A[largest]=temp
        return max_heapify(A,largest)
    return A
def heapsort(A):
    global heapsize
    heapsize=len(A)-1
    A=build_max_heap(A)
    for i in range(len(A)-1,0,-1):
        temp=A[0]
        A[0]=A[i]
        A[i]=temp
        heapsize-=1
        A = max_heapify(A,0)
    return A
