def heapsort(a):
    build_max_heap(a)
    for k in range(len(a)-1,0, -1):
        a[k], a[0]=a[0], a[k]
        max_heapify(a,0, k)

def max_heapify(a,i, heapsize):
    l=2*i+1
    r=2*i+2
    if l < heapsize and a[l]>a[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest]=a[largest], a[i] 
        max_heapify(a,largest, heapsize)

def build_max_heap(a):
    for j in range((len(a)//2)-1,-1,-1):
        max_heapify(a,j,len(a))