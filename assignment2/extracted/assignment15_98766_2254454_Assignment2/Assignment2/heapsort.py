from math import floor


def max_heapify(a, i, heapsize):
    left = 2 * (i + 1) - 1  # index
    right = 2 * (i + 1)
    if left <= heapsize - 1 and a[left] > a[i]:
        largest = left
    else:
        largest = i
    if right <= heapsize - 1 and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, heapsize)


def build_max_heap(a):
    heapsize = len(a)
    # first_parent = floor(len(a)/2) #find first parent node
    for i in range(floor(len(a) / 2) - 1, -1, -1):
        max_heapify(a, i, heapsize)


def heapsort(a):
    heapsize = len(a)
    build_max_heap(a)
    for i in range(len(a) - 1, 0, -1):  # ska det va minus 1?
        a[0], a[i] = a[i], a[0]
        heapsize = heapsize - 1
        max_heapify(a, 0, heapsize)
