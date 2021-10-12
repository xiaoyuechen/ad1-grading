import os
import array
import sys

# Bubble Sort Implementation

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False

# Insertion sort implementation
def insertionSort(a):
    ''' Sorts the array a in a non-decreasing order '''
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key

# QuickSort implementation
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

# HeapSort implementation

import math

def left(i):
    ''' Return the index of the left child'''
    return 2*i

def right(i):
    ''' Return the index of the right child'''
    return 2*i +1

def maxHeapify(a,length,i):
    ''' Makes sure the sub-tree rooted at index i is max-heap'''
    l = left(i)
    r = right(i)
    if l < length and a[l] > a[i]:
        largest = l
    else:
        largest =i

    if r < length and a[r] > a[largest]:
        largest = r
    
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a,length,largest)

def buildMaxHeap(a,length):
    ''' Builds a max-heap of array a'''
    for i in range(length//2, -1, -1):
        maxHeapify(a,length,i)


def heapSort(a):
    ''' Sorts the array a in a non-decreasing order '''
    length = len(a)
    buildMaxHeap(a, length)
    for i in range(len(a)-1,0,-1):
        a[i], a[0] = a[0], a[i]
        maxHeapify(a,i,0)



def run_bubblesort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing bubblesort
    bubblesort(a)

    # output nums_sorted.txt
    nums_sorted = open('bubblesorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

def run_insertionsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing insertion sort
    # Call your insertion sort implementation here
    insertionSort(a)

    # output nums_sorted.txt
    nums_sorted = open('insertionsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

def run_quicksort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing quicksort
    # Call your quicksort implementation here
    
    quickSort(a,0,len(a)-1)

    # output nums_sorted.txt
    nums_sorted = open('quicksorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
    heapSort(a)

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print("First create nums.txt")
        sys.exit(0)

    run_bubblesort()
    run_insertionsort()
    run_quicksort()
    run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
