import os
import array
import sys
import sort

def max_heapify(a,i,size):
        left = i*2+1
        right = i*2+2
        max = i
        if left < size and (a[max] < a[left]): #compare with left son
            max = left
        if right < size and (a[max] < a[right]):  # compare with right son
            max = right
        if max != i:
            sort.swap(a,i,max)
            max_heapify(a,max,size)

def build_max_heap(a):
    i = int(len(a)/2-1)
    while i >= 0:
        max_heapify(a,i,len(a))
        i-=1

def heapsort(a,size):
    #res = []
    build_max_heap(a)
    i = size-1
    while i >= 1:
        sort.swap(a,0,i)
        max_heapify(a,0,i)
        i -= 1

def run_heapsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing heapsort
    # Call your heapsort implementation here
    heapsort(a,len(a))

    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    if not os.path.exists('nums.txt'):
        raise FileNotFoundError('nums.txt file is not created within running folder')
    run_heapsort()


if __name__ == '__main__':
    run()

