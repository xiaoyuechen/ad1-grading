def maxheap(arr,i,length):
    #print(arr)
    left = i*2+1;
    right = i*2+2;
    largest = i;
    if left < length:
        if arr[left] > arr[i]:
            largest = left;
        else: largest=i;
    if right < length:
        if arr[right]>arr[largest]:
            largest = right;
    if largest != i:
        swap (arr, i, largest);
        maxheap(arr,largest,length);
    return;

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t