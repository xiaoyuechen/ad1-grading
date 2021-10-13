from partition import partition
def quicksort(arr,start,end):
    if start >= end:
        return;
    q = partition(arr,start,end);
    quicksort(arr,start, q-1)
    quicksort(arr,q+1,end)
