def insertionsort(A):
    
    for j in range(1, len(A)):
        key= A[j]
        i = j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i-=1
            A[i+1]=key


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
