def partition(a,p,r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1

def quicksort(a,p = 0,r = None):
    if r is None: # for deafult r
        r = len(a) - 1
    if p < r:
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
        return a


def main():
    print(quicksort([3,2,1]))

if __name__ == '__main__':
    main()
