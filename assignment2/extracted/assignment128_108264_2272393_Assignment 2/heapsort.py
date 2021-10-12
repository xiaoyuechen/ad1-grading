def swap(a,i,j):         
    a[i],a[j]=a[j],a[i]

def max_heapify(a,i,upp):    
    while (True):
        left,right=i*2+1, i*2+2
        if max(left,right)<upp:
            if a[i] >= max(a[left],a[right]): break
            elif a[left] > a[right]:
                swap(a,i,left)
                i=left
            else:
                swap(a,i,right)
                i=right
        elif left<upp:
            if a[left]>a[i]:
                swap(a,i,left)
                i=left
            else: break
        elif right<upp:
            if a[right]>a[i]:
                swap(a,i,right)
                i=right
            else: break
        else: break

def build_max_heap(a):
    for j in range((len(a)-2)//2,-1,-1):
        max_heapify(a,j,len(a))

def heapsort(a):
    build_max_heap(a)
    for end in range(len(a)-1,0,-1):
        swap(a,0,end)
        max_heapify(a,0,end)

