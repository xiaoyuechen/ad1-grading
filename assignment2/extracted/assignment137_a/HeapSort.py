def Max_Heapify(A, n, i):
    largest = i       # Initialize largest as root
    l = 2 * i + 1     # left  = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    if l<n and A[l]> A[i]:
        largest = l

    if r<n and A[r]> A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Max_Heapify(A, n, largest)


def Max_Heap(A, n):
    for i in range(n//2 -1, -1, -1):
        Max_Heapify(A, n, i)

def Heap_Sort(A):
    n = len(A)
    Max_Heap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        n-=1
        Max_Heapify(A, n, 0)
