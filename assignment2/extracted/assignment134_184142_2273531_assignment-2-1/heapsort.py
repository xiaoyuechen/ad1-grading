def heapsort(a):
      heapsize = len(a)
      buidlheap(a,heapsize)
      for i in range(heapsize-1, 0, -1):
          swap(a,i,0)
          heapify(a, i, 0)
  
def buidlheap(a,heapsize):
      for i in range(heapsize//2, -1,-1):
        heapify(a, heapsize, i)
   

def heapify(a, heapsize, i):
  largest = i
  l = 2 * i + 1
  r = 2 * i + 2
  if l < heapsize and a[i] < a[l]:
      largest = l
  if r < heapsize and a[largest] < a[r]:
      largest = r
  if largest != i:
      a[i], a[largest] = a[largest], a[i]
      heapify(a, heapsize, largest)

def swap(a,i,j):
    t = a[i]
    a[i] = a[j]
    a[j] = t




