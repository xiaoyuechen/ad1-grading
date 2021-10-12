def heapsort(a):
 n=BuildMaxHeap(a)
 for i in range(n-1,0,-1):
  a[0],a[i]=a[i],a[0]
  n-=1
  Heapify(a,i,0)
 return a
 


def BuildMaxHeap(a):
    n=len(a)
    for i in range((n//2)-1,-1,-1):
     Heapify(a,n,i)
    return n



def Heapify(a,n,i):
 left=2*i
 right=2*i+1
 if left<=n-1 and a[left]>a[i]:
     Max=left
 else:
   Max=i


 if right<=n-1 and a[right]>a[Max]:
  Max=right

 if Max!=i:
    a[i],a[Max]=a[Max],a[i]
    Heapify(a,n,Max)
