def partition(a,low,high):
    ''' Partitions the array a into two subarrays'''
    pivot = a[high]
    i = low-1

    for j in range(low,high):
        if a[j] <= pivot:
            i+=1
            a[i], a[j] = a[j], a[i]

    a[i+1], a[high] = a[high], a[i+1]
    return i + 1
    
def quickSort(a,low,high):
    ''' Sorts the array a in a non-decreasing order '''

    # If len(a) == 1 -> array already sorted
    if len(a) == 1:
        return a
    if low < high:
        q = partition(a,low,high)
        quickSort(a,low,q-1)
        quickSort(a,q+1,high)


