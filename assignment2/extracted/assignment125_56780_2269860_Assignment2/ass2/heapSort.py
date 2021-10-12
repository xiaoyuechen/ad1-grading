
def left(i):
    ''' Return the index of the left child'''
    return 2*i 

def right(i):
    ''' Return the index of the right child'''
    return 2*i +1

def maxHeapify(a,length,i):
    ''' Makes sure the sub-tree rooted at index i is max-heap'''
    l = left(i)
    r = right(i)
    if l < length and a[l] > a[i]:
        largest = l
    else:
        largest =i

    if r < length and a[r] > a[largest]:
        largest = r
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a,length,largest)

def buildMaxHeap(a,length):
    ''' Builds a max-heap of array a'''
    for i in range(length//2, -1, -1):
        maxHeapify(a,length,i)


def heapSort(a):
    ''' Sorts the array a in a non-decreasing order '''
    length = len(a)
    buildMaxHeap(a, length)
    for i in range(len(a)-1,0,-1):
        a[i], a[0] = a[0], a[i]
        maxHeapify(a,i,0)


A = [11, 34, 9, 5, 16, 10, 2123, 0, 21, 19] 
heapSort(A)
print(A)
