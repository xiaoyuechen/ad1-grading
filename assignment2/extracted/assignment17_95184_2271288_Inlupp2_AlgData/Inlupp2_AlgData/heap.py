import math as m

def max_heapify(A:list,heap_size:int,i:int):
    left = 2*i + 1
    right = 2*i + 2

    if left < heap_size and A[left] > A[i]:
        largest = left
    else:
        largest = i
    
    if right < heap_size and A[right] > A[largest]:
        largest = right
    
    if largest != i:
        spare = A[i]
        A[i] = A[largest]
        A[largest] = spare
        max_heapify(A, heap_size, largest)


def build_max_heap(A):

    for i in range(m.floor(len(A)/2)-1, -1, -1):
        max_heapify(A,len(A),i)


def heapsort(A):

    build_max_heap(A)
    for i in range(len(A)-1, 0,-1):
        spare = A[0]
        A[0] = A[i]
        A[i] = spare
        max_heapify(A, i, 0)

if __name__ == '__main__':
    test = [7, 1, 9, 3]
    heapsort(test)
    print(test)