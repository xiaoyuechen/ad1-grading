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
    def insertionSort(a):
        for i in range(1, len(a)):
            index = a[i]
            j = i - 1
            # index i = 1 0ch index j = 2
            while j >= 0 and index < a[j]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = index
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
    def partition(array, start, end):
        pivotPoint = array[start]
        smaller = start + 1
        higher = end

        while True:
            while smaller <= higher and array[higher] >= pivotPoint:
                higher = higher - 1
            # go from last index and compare to pivot until index is smaller than pivot
            while smaller <= higher and array[smaller] <= pivotPoint:
                smaller = smaller + 1
            # go from first index and compare to pivot until index is bigger than pivot
            if smaller <= higher:
                swap(array, smaller, higher)
                # change places of the indexes
            else:
                break

        swap(array, start, higher)
        # change positions of smaller and higher one last time

        return higher

    def quickSort(array, start, end):
        if start >= end:
            return

        p = partition(array, start, end)
        quickSort(array, start, p - 1)
        quickSort(array, p + 1, end)

    quickSort(a, 0, len(a)-1);

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
    def MaxHeapify(array, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and array[i] < array[l]:
            largest = l

        if r < n and array[largest] < array[r]:
            largest = r

        if largest != i:
            swap(a, largest, i)
            MaxHeapify(array, n, largest)

    def heapSort(a):
        n = len(a)

        # Build max heap
        for i in range(n // 2, -1, -1):
            MaxHeapify(a, n, i)

        for i in range(n - 1, 0, -1):
            # Swap
            swap(a, 0, i)

            MaxHeapify(a, i, 0)

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
        print( "First create nums.txt");
        sys.exit(0)

    run_bubblesort()
    run_insertionsort()
    run_quicksort()
    run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
