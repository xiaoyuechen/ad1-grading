import os
import array
import sys



def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def max_heapify(a,i,heapsize):
    L = 2*i + 1
    R = 2*i + 2
    if L <= heapsize-1 and a[L] > a[i]:
        largest = L
    else:
        largest = i
    if R <= heapsize-1 and a[R] > a[largest]:
        largest = R
    if largest != i:
        swap(a,i,largest)
        max_heapify(a,largest,heapsize)

def build_max_heap(a):
    heapsize = len(a)
    for i in reversed(range(0,len(a)//2)):
        max_heapify(a,i,heapsize)

def heapsort(a):
    build_max_heap(a)
    heapsize = len(a)
    for i in reversed(range(1,len(a))):
        swap(a,0,i)
        heapsize -= 1
        max_heapify(a,0,heapsize)

def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
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
        print("First create nums.txt")
        sys.exit(0)

    run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
