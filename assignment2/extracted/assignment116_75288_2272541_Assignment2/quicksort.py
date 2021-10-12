def partition(a,p,r):
    x = a[r]
    i = p - 1
    for j in range(p,r):
        if a[j] <= x:
            i = i + 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[i+1]
    a[i+1] = a[r]
    a[r] = temp
    return i+1
    
def _quicksort(a,p,r):
    if p < r:
        q = partition(a,p,r)
        _quicksort(a,p,q-1)
        _quicksort(a,q+1,r)
    return a

def quicksort(a):
    return _quicksort(a,0,len(a)-1)