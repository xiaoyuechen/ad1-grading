def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def max_heapify(a, i, heap_size):
    # Compare A[i], A[left(i)], A[right(i)]
    left = i*2 + 1
    right = i*2 + 2
    if left < heap_size and a[left] > a[i]:
        largest = left
    else:
        largest = i
    if right < heap_size and a[right] > a[largest]:
        largest = right
    if largest != i:
        swap(a, i, largest)
        max_heapify(a, largest, heap_size)

def build_max_heap(a):
    heap_size = len(a)
    for i in range(heap_size//2 - 1, -1, -1):
        max_heapify(a, i, heap_size)

def heapsort(a):
    build_max_heap(a)
    heap_size = len(a)
    for i in range(heap_size - 1, 0, -1):
        swap(a, 0, i)
        heap_size -= 1
        max_heapify(a, 0, heap_size)