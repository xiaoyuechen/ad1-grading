def max_heapify(A, i, heapsize):
    l = 2*i+1
    r = 2*i+2
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heapsize)
        
def build_max_heap(A, heapsize):
    for i in range(heapsize//2-1, -1, -1):
        max_heapify(A, i, heapsize)

def heapsort(A):
	heapsize = len(A)
	build_max_heap(A, heapsize)
	for i in range(heapsize-1, 0, -1):
		A[i], A[0] = A[0], A[i]
		heapsize -= 1
		max_heapify(A,0,heapsize)
	return (A)