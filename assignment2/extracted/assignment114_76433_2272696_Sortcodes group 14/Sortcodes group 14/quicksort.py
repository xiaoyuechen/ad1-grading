
import os
import sys

# Implementation of Quicksort
# Group 14

def swap(array, i, j):

    save = array[i]
    array[i] = array[j]
    array[j] = save

    return array


def partition(array, start, end):

    pivot_element = array[end]
    i = start - 1

    for j in range(start, end):

        if array[j] <= pivot_element:
            i += 1
            array = swap(array, i, j)

    array[end] = array[i + 1]
    array[i + 1] = pivot_element

    return i + 1


def quicksort(array, start, end):

    if start < end:
        q = partition(array, start, end)
        quicksort(array, start, q - 1)
        quicksort(array, q + 1, end)

    return array


# Note: Including the run function so that module can be run stand-alone
# We were not sure if this was needed based on the assignment


def run_quicksort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing quicksort
    # Call your quicksort implementation here
    a = quicksort(a, 0, len(a) - 1)

    # output nums_sorted.txt
    nums_sorted = open('quicksorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()

def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print("First create nums.txt")
        sys.exit(0)

    run_quicksort()


if __name__ == "__main__":
    run()
