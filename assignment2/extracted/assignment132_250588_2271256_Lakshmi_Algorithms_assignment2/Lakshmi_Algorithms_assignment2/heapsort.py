###--------------Heapsort Algorithm Implementation in Python-----------------###
#Reads nums.txt file created by rangen.py and sorts the value using heapsort algorithm
#Output:Creates a heapsorted.txt file and writes the sorted value to the text file
#To compile: python heapsort.py


import os
import array
import sys

# Swap Function

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t

#Maxifying the heap functiom
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


#Building Maxheap function
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

#For calling heapsort function and creates a heapsorted.txt file
def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    HeapSort(a)

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
    run_heapsort()

if __name__ == "__main__":
    run()
