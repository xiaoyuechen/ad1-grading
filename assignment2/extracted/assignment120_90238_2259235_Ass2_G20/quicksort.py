def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def quicksort(a, start, end):
    if start < end:
        q = partition(a, start, end)
        quicksort(a, start, q-1)
        quicksort(a, q, end)

def partition(a, start, end):
    x = a[end]
    i = start - 1
    for j in range(start, end):
        if a[j] <= x:
            i += 1
            swap(a, i, j)
    swap(a,i+1,end)
    return i + 1