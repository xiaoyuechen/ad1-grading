def quick_sort(A,p,r):
    if p<r:
        q=partition_sort(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
    return A


def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

def partition_sort(A,p,r):
    x=A[r]          
    i=p-1      
    for j in range(p, r):
        if x>=A[j]:             
            i+=1
            swap(A,i,j)
    swap(A, i+1, r)
    return i+1

