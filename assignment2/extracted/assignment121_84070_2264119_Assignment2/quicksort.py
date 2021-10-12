def Partition(A,p,r):
    x= A[r]
    i= p-1
    
    for j in range(p, r):
        if A[j]<=x:
            i=i+1
            #swap A[i] and A[j]
            key=A[i]
            A[i]=A[j]
            A[j]=key
    #swap A[i+1] and A[r]
    key= A[i+1]
    A[i+1]= A[r]
    A[r]=key
    return i+1
    
def QuickSort(A,p,r):
    
    if p<r:
        q= Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

def quicksort(A):
    p=0
    r= len(A)-1
    QuickSort(A,p,r)
    
    

