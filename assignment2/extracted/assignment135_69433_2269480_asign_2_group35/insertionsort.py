

def insertionSort(Array):


    for j in range(1,len(Array)):
        key = Array[j]
        i = j-1
        while i > -1 and Array[i] > key:
            Array[i+1] = Array[i]
            i = i-1
        Array[i+1] = key

   




