def MaxHeapify(A,i):
    l = (i*2) +1
    r = (i*2) +2
    largest = i
    if l < hs:
        if A[l] >= A[i]:
            largest = l
    if r < hs:
        if A[r] >= A[largest]:
            largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        MaxHeapify(A,largest)
    return

def BuildMaxHeap(A):
    global hs
    hs = len(A)
    for i in range(len(A)//2,-1, -1):
        MaxHeapify(A,i)
    return

def HeapSort(A):
    BuildMaxHeap(A)
    for i in range(len(A)-1,-1,-1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        global hs
        hs = hs-1
        MaxHeapify(A,0)
    return

