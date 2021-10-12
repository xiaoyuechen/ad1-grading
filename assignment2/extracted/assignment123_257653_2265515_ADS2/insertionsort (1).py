

import os
import array
import sys

def inssort(array):
    j = 1
    while j < len(array):
        key = array[j]
        i = j - 1
        while i > -1 and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        array[i + 1] = key
        j += 1

def run_insertionsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))
    
    # Testing insertion sort
    inssort(a)
    # Call your insertion sort implementation here
    # inssort(a)

    # output nums_sorted.txt
    nums_sorted = open('insertionsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")
    nums.close()
    nums_sorted.close()

def run():
    if not os.path.exists('nums.txt'):
        raise FileNotFoundError('nums.txt file is not created within running folder')
    run_insertionsort()


if __name__ == '__main__':
    run()




