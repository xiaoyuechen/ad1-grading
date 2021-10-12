
import os
import sys
import math

# Implementation of Heapsort
# Group 14

def swap(array, i, j):

    save = array[i]
    array[i] = array[j]
    array[j] = save

    return array


def max_heapify(array, heap_size, i):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and array[left] > array[i]:
        largest = left
    else:
        largest = i

    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != i:
        array = swap(array, i, largest)
        array = max_heapify(array, heap_size, largest)

    return array


def build_max_heap(array):
    heap_size = len(array)

    i = math.floor(heap_size / 2) - 1
    while i >= 0:
        array = max_heapify(array, heap_size, i)
        i -= 1

    return array, heap_size


def heapsort(array):
    array, heap_size = build_max_heap(array)

    i = len(array) - 1
    while i >= 1:
        array = swap(array, i, 0)
        heap_size -= 1
        array = max_heapify(array, heap_size, 0)
        i -= 1

    return array


# Note: Including the run function so that module can be run stand-alone
# We were not sure if this was needed based on the assignment


def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
    a = heapsort(a)

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


if __name__ == "__main__":
    run()
