
import os
import sys

# Implementation of Insertion sort
# Group 14

def insertion_sort(array):

    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1

        array[i + 1] = key

    return array

# Note: Including the run function so that module can be run stand-alone
# We were not sure if this was needed based on the assignment


def run_insertionsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing insertion sort
    # Call your insertion sort implementation here
    a = insertion_sort(a)

    # output nums_sorted.txt
    nums_sorted = open('insertionsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print("First create nums.txt")
        sys.exit(0)

    run_insertionsort()


if __name__ == "__main__":
    run()
