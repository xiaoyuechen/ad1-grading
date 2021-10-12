def inssort(A):
    sorted=False
    while not sorted:
        sorted=True
        for j in range(1, len(A)):
            key=A[j]
            i=j-1
            while i>=0 and A[i]>key:
                A[i+1]=A[i]
                i=i-1
                sorted=False
            A[i+1]=key
