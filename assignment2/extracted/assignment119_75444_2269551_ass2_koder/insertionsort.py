def insertionsort(A):
    for j in range(len(A)):
        key=A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
                
