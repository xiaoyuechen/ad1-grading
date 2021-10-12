import array
import math



def maxHeapify(a,i, heapSize):
	l = 2*i
	r = 2*i+1
	if l < heapSize and a[l]>a[i]:
		largest = l
	else:
		largest = i

	if r < heapSize and a[r]>a[largest]:
		largest = r
	if largest != i:
		a[i], a[largest] = a[largest], a[i]
		maxHeapify(a, largest,heapSize)

def buildMaxHeap(a):
	heapSize = len(a)
	for i in range(math.floor(len(a)/2)-1, -1,-1):
		maxHeapify(a, i, heapSize)

def heapsort(a):
	buildMaxHeap(a)
	heapSize = len(a)
	for i in range(len(a)-1, -1 ,-1):
		a[0], a[i] = a[i], a[0] 
		heapSize= heapSize-1
		maxHeapify(a,0, heapSize)



