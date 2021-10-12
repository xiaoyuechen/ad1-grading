###-------------Insertionsort Algorithm Implementation in Python-------------####Reads nums.txt file created by rangen.py and sorts the elements using insertionsort algorithm
#Output:Creates a insertionsorted.txt file and writes the sorted value to the text file.
#To Compile: python insertionsort.py

import os
import array
import sys

# Swap Function

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

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

#Function to call insertionsort and create insertionsort.txt file
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

#For running the function
def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print('First create nums.txt')
        sys.exit(0)
    run_insertionsort()

if __name__ == "__main__":
    run()

