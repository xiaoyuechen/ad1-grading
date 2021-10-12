

def Partion(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <=x:
            i = i+1
            ex = A[i]
            A[i] = A[j]
            A[j] = ex
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1


def QuickSort(A,p,r):
    
    if p < r:
        q = Partion(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
    return 


