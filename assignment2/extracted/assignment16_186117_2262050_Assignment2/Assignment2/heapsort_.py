def max_heapify(lst, heap_size, i):
    l = 2*i + 1
    r = 2*i + 2
    if l <= heap_size and lst[l] > lst[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and lst[r] > lst[largest]:
        largest = r
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        max_heapify(lst, heap_size, largest)

def build_max_heap(lst):
    heap_size = len(lst)
    index_last_parent = (len(lst) - 2) // 2
    for i in range(index_last_parent, -1, -1):
        max_heapify(lst, heap_size - 1, i)      # heap_size - 1 because we are really comparing indexes...

def heapsort(lst):
    build_max_heap(lst)
    heap_size = len(lst)
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heap_size -= 1
        max_heapify(lst, heap_size - 1, 0)