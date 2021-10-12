def partition(A,first,last):
    pivot=A[last]
    i=first-1
    for index in range(first,last):
        if A[index]<=pivot:
            i+=1
            temporary=A[i]
            A[i]=A[index]
            A[index]=temporary
    temporary=A[i+1]
    A[i+1]=A[last]
    A[last]=temporary
    return i+1

def quicksorting(A,first,last):
    if first < last:
        i_pivot=partition(A,first,last)
        quicksorting(A,first,i_pivot-1)
        quicksorting(A,i_pivot+1,last)

def quicksort(A):
    first=0
    last=len(A)-1
    quicksorting(A,first,last)
