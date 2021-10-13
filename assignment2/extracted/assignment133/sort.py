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

def inssort(a):
    for i in range(1, len(a)):
 	key = a[i]
        j = i-1
        while j >= 0 and key < a[j] :
                a[j + 1] = a[j]
                j -= 1
        a[j + 1] = key

def partition(a, low, high):
    i = (low-1)
    pivot = a[high]
    for j in range(low, high):
        if a[j] <= pivot:
            i = i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return (i+1)

def quicksort(a, low, high):
    if len(a) == 1:
        return a
    if low < high:
        pi = partition(a, low, high)
        quicksort(a, low, pi-1)
        quicksort(a, pi+1, high)
def max_heapify(a, n, i):
    largest = i; # Initialize largest as root
    l = 2 * i + 1; # left = 2*i + 1
    r = 2 * i + 2; # right = 2*i + 2
    if l < n and a[l] > a[largest]:
        largest = l;
    if r < n and a[r] > a[largest]:
        largest = r;
    if largest != i:
        a[i], a[largest] = a[largest], a[i];
        max_heapify(a, n, largest);

def buildheap(a,n):

    # Index of last non-leaf node
    startIdx = n // 2 - 1;
    for i in range(startIdx, -1, -1):
        max_heapify(a, n, i);

def heapsort(a):
	buildheap(a)
	for i   a: length downto 2:
		temp=a[0]
		a[0]=a[i]
		a[i]=temp
		max_heapify(a,1)
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
    # inssort(a)

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
    low=0
    high=len(a)-1
    quicksort(a,low,high)

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
    # heapsort(a)

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print "First create nums.txt"
        sys.exit(0)

    run_bubblesort()
    run_insertionsort()
    run_quicksort()
    run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
