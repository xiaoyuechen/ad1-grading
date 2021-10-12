
def partition(A:list, p:int, r:int):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            spare = A[i]
            A[i] = A[j]
            A[j] = spare
    spare = A[i+1]
    A[i+1] = A[r]
    A[r] = spare
    
    return i+1


def _quicksort(A:list, p:int, r:int):
    if p < r:
        q = partition(A, p, r)
        _quicksort(A,p,q-1)
        _quicksort(A, q+1, r)


def quicksort(A):
    p = 0
    r = len(A) - 1 
    _quicksort(A, p, r)

if __name__ == '__main__':
    test = [7,9,5,1]

    quicksort(test)
    print(test)