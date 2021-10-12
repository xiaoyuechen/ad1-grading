def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            temp_j = A[j]
            temp_i = A[i]
            A[i] = temp_j
            A[j] = temp_i
    temp_r = A[r]
    temp_i = A[i+1]
    A[r] = temp_i
    A[i+1] = temp_r
    return i + 1
    

def QuickSort(A, p, r):
    if (p < r):
        q = partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)
        
