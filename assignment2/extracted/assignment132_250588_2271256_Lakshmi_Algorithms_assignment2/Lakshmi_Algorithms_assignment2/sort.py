###--------The Program to Sort the values of nums.txt using Pyhton-----------########-------Using Bubblesort,Insertionsort,Quicksort and Heapsort---------######
#Reads the value of nums.txt file and sorts the values using all the algorithms
#Output: Creates four text files- bubblesorted.txt,insertionsorted.txt,quicksorted.txt,heapsorted.txt. Sorted values by each algorithms are written to the respective text file

import os
import array
import sys

# Swap Function

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


#Bubble sort function
def bubblesort(a):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                swap(a, i, i+1)
                sorted = False


#Calls bubblesort function and creates bubblesort.txt file
def run_bubblesort():
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))
    bubblesort(a)
    nums_sorted = open('bubblesorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


#Insertionsort function
def InsertionSort(arr):
        len_arr = len(arr)
        for j in range(1,len_arr):
                key = arr[j]
                i = j-1
                while i>=0 and arr[i] > key:
                        arr[i+1] = arr[i]
                        i = i-1
                        arr[i+1] = key


#Calls insertionsort function and creates insertionsorted.txt file
def run_insertionsort():
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))
    InsertionSort(a)
    nums_sorted = open('insertionsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


#Partition function for quicksort
def Partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if a[j]<=x:
                i = i+1
                swap(a,i,j)
    swap(a,i+1,r)
        #a[i+1],a[r] = a[r],a[i+1]
    return (i+1)


#Quick sort function
def QuickSort(arr,FirstElement,LastElement):
    if FirstElement < LastElement:
        PivotElement = Partition(arr,FirstElement,LastElement)
        #print("pivo %d" % PivotElement)
        QuickSort(arr,FirstElement,PivotElement-1)
        QuickSort(arr,PivotElement+1,LastElement)
       #return(arr)

#Calls quicksort function and creates quicksorted.txt file
def run_quicksort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    len_a = len(a)
    First = 0
    Last = len_a - 1

    QuickSort(a,First,Last)
    # quicksort(a)

    # output nums_sorted.txt
    nums_sorted = open('quicksorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")
    nums.close()
    nums_sorted.close()


#Maxheap function for heapsort
def Max_Heapify(A,i,len_A):
    left_i = 2*i+1
    right_i = 2*i+2
    large = i
    if left_i < len_A and A[left_i] > A[i]:
        large = left_i
    if right_i < len_A and A[right_i] > A[large]:
        large = right_i
    if large != i:
        swap(A,i,large)
            #A[i],A[large] = A[large],A[i]
        Max_Heapify(A,large,len_A)


#Build max haeap function for heapsort
def BuildMax_Heap(B):
    len_B = len(B)
    B_HeapSize = len_B
    for j in range(len_B/2+1, -1, -1):
        Max_Heapify(B,j,len_B)

#Heapsort function
def HeapSort(arr):
    len_arr = len(arr)
    BuildMax_Heap(arr)
    for k in range(len_arr-1, 0, -1):
        swap(arr,0,k)
        #arr[0],arr[k] = arr[k],arr[0]
        #len_arr -= 1
        Max_Heapify(arr,0,k)

#Calls heapsort function and creates heapsorted.txt file
def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    HeapSort(a)

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print('First create nums.txt')
        sys.exit(0)
    #Calls all the four sorting algorithms
    run_bubblesort()
    run_insertionsort()
    run_quicksort()
    run_heapsort()

if __name__ == "__main__":
    run()

