###---------------Quicksort Algorithm Implementation in Python---------------###
#Reads nums.txt created by rangen.py and sorts the elements using quicksort algorithm#
#Ouput: Creates quicksorted.txt and writes the sorted values to the test file#
#To Compile:python quicksort.py

import os
import array
import sys

# Swap Function

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

#Partition Function
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

#Quicksort Function
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
    nums_sorted = open('quicksorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print('First create nums.txt')
        sys.exit(0)
    run_quicksort()

if __name__ == "__main__":
    run()
