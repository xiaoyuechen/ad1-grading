def inssort(a):

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j > -1 and key < a[j]:

            a[j+1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a 
