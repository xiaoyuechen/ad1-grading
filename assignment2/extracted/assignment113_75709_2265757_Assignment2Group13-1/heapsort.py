import os
import array
import sys

def build_max_heap(A, n):
    for i in range(n//2 - 1, -1, -1):
        max_heapify(A, n, i)

def max_heapify(A, n, i):
    largest = i  
    left = (2 * i) + 1    
    right = (2 * i) + 2 

    if left < n and A[largest] < A[left]:
        largest = left

    if right < n and A[largest] < A[right]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i] 
        max_heapify(A, n, largest) 

def heap_sort(A):
    n = len(A)
    build_max_heap(A, n)
    
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)
    return A

def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
    # heapsort(a)
    a = heap_sort(a)

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

    run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
