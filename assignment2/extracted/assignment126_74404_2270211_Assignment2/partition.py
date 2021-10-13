def partition (arr,start,end):
    pivot = arr[end];
    i = start-1;
    for j in range(start,end):
        if arr[j]<=pivot:
            i +=1;
            swap(arr,i,j);
    swap(arr,i+1,end);
    return i+1;

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t
