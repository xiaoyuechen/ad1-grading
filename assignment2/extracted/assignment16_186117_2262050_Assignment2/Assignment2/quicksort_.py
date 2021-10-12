def partition(lst, p, r):
    x = lst[r]
    i = p - 1
    for j in range(p, r):
        if lst[j] <= x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[r] = lst[r], lst[i+1]

    return i + 1

def quicksort(lst, p, r):
    if p < r:
        q = partition(lst, p, r)
        quicksort(lst, p, q - 1)
        quicksort(lst, q + 1, r)