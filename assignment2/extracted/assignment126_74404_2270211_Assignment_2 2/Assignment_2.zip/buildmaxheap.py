from maxheap import maxheap
def buildmaxheap(arr,length):
    heapsize = len(arr)-1;
    for i in range (int(heapsize/2), -1 , -1):
        maxheap(arr,i,length);
        #print(arr)
    #print(arr)
    return;