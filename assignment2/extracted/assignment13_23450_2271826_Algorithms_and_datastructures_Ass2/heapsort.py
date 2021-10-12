# Find the correct indices
def left(i):
    return (2*(i+1))-1
def right(i):
    return (2*(i+1)+1)-1
def parent(i):
    return(i//2) #Rounds down

def build_max_heap(a):
    start = (len(a)//2)-1
    for i in range(start, -1, -1): # Reverse order down to 0
        max_heapify(a, i, len(a)-1)

def max_heapify(a, i, heap_size):
    l = left(i)
    r = right(i)
    largest = i
    # Find index j for which a[j] is largest
    if l <= heap_size: # So we don't go out of list index
        if a[largest] < a[l]:
            largest = l
    if r <= heap_size: # So we don't go out of list index
        if a[largest] < a[r]:
            largest = r
    # If a child is larger than the parent
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest, heap_size)

def heapsort(a):
    build_max_heap(a)
    # heap_size = len(a) -1
    # while heap_size > 0:
    for heap_size in range(len(a)-1, -1, -1):  # Reverse order down to 0
        a[0], a[heap_size] = a[heap_size], a[0]
        max_heapify(a, 0, heap_size-1)