# Quick Sort Implementation
def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            swap(a, i, j);
    swap(a, (i + 1), r)
    return i + 1

def quicksort_do(a,p,r):
    if p < r:
        q = partition(a, p, r)
        quicksort_do(a, p, (q - 1))
        quicksort_do(a, (q + 1), r)

def quicksort(a):
    p = 0
    r = len(a)-1
    quicksort_do(a,p,r)    
    