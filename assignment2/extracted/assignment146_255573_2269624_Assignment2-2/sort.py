import os
import array
import sys


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


def inssort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            swap(a, i, j)
    swap(a, i + 1, r)
    return (i + 1)


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


def max_heapify(a, i, heap_size):
    l = 2 * i + 1 # left child
    r = 2 * i + 2 # right child
    if l < heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a, i, largest)
        max_heapify(a, largest, heap_size)


def build_max_heap(a):
    for i in range((len(a) // 2) - 1, -1, -1):
        max_heapify(a, i, len(a))


def heapsort(a):
    build_max_heap(a)
    heap_size = len(a)
    for i in range(len(a) - 1, 0, -1):
        swap(a, 0, i)
        heap_size -= 1
        max_heapify(a, 0, heap_size) # where heap_size is used for shorten the array during max_heapify


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

    inssort(a)

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

    p = 0
    r = len(a) - 1
    quicksort(a, p, r)

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

    heapsort(a)

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print ("First create nums.txt")
        sys.exit(0)

    run_bubblesort()
    run_insertionsort()
    run_quicksort()
    run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
