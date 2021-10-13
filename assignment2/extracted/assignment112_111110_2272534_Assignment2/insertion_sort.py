import os
import array
import sys

# Bubble Sort Implementation

def swap(a, i, j):
    t = a[j]
    a[j] = a[i]
    a[i] = t


def insertionsort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i-1
        while j>=0 and temp<a[j]:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp


def run_insertionsort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing insertion sort
    # Call your insertion sort implementation here
    # inssort(a)
    insertionsort(a)

    # output nums_sorted.txt
    nums_sorted = open('insertionsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()



def run():
    # check if nums.txt exists
    if not os.path.exists('nums.txt'):
        print ("First create nums.txt")
        sys.exit(0)

    
    run_insertionsort()
 


# python sort.py runs run
if __name__ == "__main__":
    run()
