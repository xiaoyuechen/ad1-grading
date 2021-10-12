def partition(a, p=0, r=None):
    if r is None:
        r = len(a)-1
    pivot = a[r]
    i = p-1
    for j in range(p, r+1):
        if j == r:  # Do last switch
            a[r], a[i+1] = a[i+1], a[r]
        elif a[j] <= a[r]:
            i += 1
            a[j], a[i] = a[i], a[j]
    return i+1

def quicksort(a, p=0, r=None):
    if r is None:
        r = len(a) - 1
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)