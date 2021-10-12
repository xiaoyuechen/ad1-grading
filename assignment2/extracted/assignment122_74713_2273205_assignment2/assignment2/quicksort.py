def quicksort(a, p = 0, r = None):

    if r == None:
        r = len(a) - 1
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)
    return a

def partition(a, p, r):
    
    key = a[r]
    k = p - 1
    for i in range(p, r):
        if a[i] <= key:
            k += 1
            temp = a[k]
            a[k] = a[i]
            a[i] = temp
    a[r] = a[k+1]
    a[k+1] = key
    return k + 1
