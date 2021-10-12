def max_heapify(Array, i, length):
    largest = i
    leftChild = 2*i+1
    rightChild = 2*i+2

    if leftChild < length and Array[i] < Array[leftChild]:
        largest = leftChild
        

    if rightChild < length and Array[largest] < Array[rightChild]:
        largest = rightChild
        
    if largest !=i:
        Array[i], Array[largest] = Array[largest], Array[i]
        max_heapify(Array, largest, length)
        

def build_max_heap(Array, length):
    for i in range(length//2-1, -1, -1):
        max_heapify(Array, i, length)

def heap_sort(Array):
    
    length = len(Array)
    build_max_heap(Array, length)

    for i in range(length-1, 0, -1):
        Array[i], Array[0] = Array[0], Array[i]
        max_heapify(Array, 0, i)

    return Array
