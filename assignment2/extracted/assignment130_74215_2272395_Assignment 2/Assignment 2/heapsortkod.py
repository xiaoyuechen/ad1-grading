def max_heapify(A,i, length):

    largest=i
    #lenght=len(A)
    left=2*i+1 #left child
    right=2*i+2 #right child


    if left<length and A[left]>A[i]:
        largest=left

    if right< length and A[right]>A[largest]:
        largest=right

    if largest !=i:
        A[i],A[largest]=A[largest],A[i]
        max_heapify(A,largest, length)


def build_max_heap(A,length):
    for i in range(length//2-1, -1, -1):
        max_heapify(A,i, length)


def heapsort(A):
    length=len(A)
    build_max_heap(A, length)
    for i in range(length-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, 0, i)

    return A


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
