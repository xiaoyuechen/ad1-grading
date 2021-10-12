import os
import array
import sys


def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r ):
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


def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print ("First create nums.txt")
        sys.exit(0)

    run_quicksort()


# python sort.py runs run
if __name__ == "__main__":
    run()

