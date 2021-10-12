def swap(arr, i, j):
    """ Swap position of arr[i] and arr[j]"""
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            swap(arr, i, j)
    swap(arr, i+1, r)
    return i + 1


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)
