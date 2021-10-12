import os
import array
import sys
import random

def rangen(max):
    f = open('nums.txt', 'w')
    random.seed()

    for i in range(0,max):
        f.write(str(random.randint(0, max)) + "\n")

    f.close()


def insertionsort(s):
    for i in range(1,len(s)):
        key=s[i]
        j=i-1
        while j>=0 and key<s[j]:
            s[j+1]=s[j]
            j=j-1
        s[j+1] = key

def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
        if a[j]<=x:
            i=i+1
            changer1=a[i]
            a[i]=a[j]
            a[j]=changer1
    changer2=a[r]
    a[r]=a[i+1]
    a[i+1]=changer2
    return i+1

def quicksort(a,p,r):
    if p<r:
        q=partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)



def heapsort(a):
    n=len(a)
    for i in range(n//2 - 1, -1, -1):
        maxheapify(a, n, i)
    for i in range(n-1,0,-1):
        buildmaxheap(a,i)




def buildmaxheap(a,i):
    a[i],a[0]=a[0],a[i]
    maxheapify(a,i,0)






def maxheapify(a,n,i):
    largest = i
    l=2*i+1
    r=2*i+2

    if l<n and a[largest]<a[l]:
        largest=l

    if r<n and a[largest]<a[r]:
        largest=r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]

        maxheapify(a,n,largest)
        


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

def run_quicksort():
    # read the content of nums.txt into an array
    nums = open('nums.txt', 'r')
    a = []
    for line in nums:
        a.append(int(str.strip(line)))

    # Testing quicksort
    # Call your quicksort implementation here
    # quicksort(a)
    quicksort(a,0,len(a)-1)
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
    heapsort(a)
    # output nums_sorted.txt
    nums_sorted = open('heapsorted.txt', 'w')
    for element in a:
        nums_sorted.write(str(element) + "\n")

    nums.close()
    nums_sorted.close()


def run():
    # check if nums.txt exists
    rangen(100)
    if not os.path.exists('nums.txt'):
        print ("First create nums.txt")
        sys.exit(0)
    run_insertionsort()
    run_quicksort()
    run_heapsort()


# python sort.py runs run
if __name__ == "__main__":
    run()
