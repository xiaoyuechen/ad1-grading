def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def max_heapify(a, i, heap_size):
    l = 2*i + 1
    r = 2*i + 2
    if l < heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a, i, largest)
        max_heapify(a, largest, heap_size)

def build_max_heap(a):
    heap_size = len(a)
    for i in range(int(len(a)/2), -1, -1):
        max_heapify(a, i, heap_size)

def heapsort(a):
    heap_size = len(a)
    build_max_heap(a)
    for i in range(len(a)-1, 0, -1):
        swap(a, 0, i)
        heap_size = heap_size - 1
        max_heapify(a, 0, heap_size)