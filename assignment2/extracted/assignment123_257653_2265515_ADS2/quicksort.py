import os


def quicksort_wrapper(array):
    return quicksort(array, 0, len(array) - 1)


def quicksort(array, start, end):
    if end > start:
        q = partition(array, start, end)
        quicksort(array, start, q - 1)
        quicksort(array, q + 1, end)


def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


def run_quicksort():
    nums = open('nums.txt', 'r')
    arr = [int(str.strip(num)) for num in nums]
    nums.close()
    quicksort_wrapper(array=arr)

    nums_sorted = open('quicksort.txt', 'w')
    for element in arr:
        nums_sorted.write(str(element) + "\n")
    nums_sorted.close()


def run():
    if not os.path.exists('nums.txt'):
        raise FileNotFoundError('nums.txt file is not created within running folder')
    run_quicksort()


if __name__ == '__main__':
    run()

