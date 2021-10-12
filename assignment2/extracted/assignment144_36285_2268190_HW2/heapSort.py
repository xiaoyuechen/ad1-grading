def swap(arr, i, j):
    """ Swap position of arr[i] and arr[j]"""
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def max_heapify(arr, heap_size, i):
    l = 2*i + 1
    r = 2*i + 2

    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        swap(arr, i, largest)
        max_heapify(arr, heap_size, largest)

def build_max_heap(arr):
    heap_size = len(arr)
    for i in range((heap_size // 2) -1, -1, -1):
        max_heapify(arr, heap_size, i)

def heap_sort(arr):
    build_max_heap(arr)
    heap_size = len(arr)
    for i in range(len(arr)-1, 0, -1):
        swap(arr, 0, i)
        heap_size = heap_size -1
        max_heapify(arr, heap_size, 0)


