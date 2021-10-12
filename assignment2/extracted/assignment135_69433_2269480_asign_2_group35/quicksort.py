


def quickSort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    return A

    
def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            swap(A, i, j)
    swap(A, i+1, r)
    i = i+1
    return i
            

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t




