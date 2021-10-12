import sys

class heapsort:

    def __init__(self, a):
        self.__a = a.copy()
        self.__a = self.__sort()

    def __max_heapify(self, heap_size, i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left < heap_size and self.__a[left] > self.__a[largest]:
            largest = left

        if right < heap_size and self.__a[right] > self.__a[largest]:
            largest = right

        if largest != i:
            self.__a[i], self.__a[largest] = self.__a[largest], self.__a[i]
            self.__max_heapify(heap_size, largest)

    def __build_max_heap(self):
        heap_size = len(self.__a)
        for i in range(heap_size//2 - 1, -1, -1):
            self.__max_heapify(heap_size, i)
        return heap_size

    def __sort(self):
        heap_size = self.__build_max_heap()
        for i in range(heap_size-1, 0, -1):
            self.__a[0], self.__a[i] = self.__a[i], self.__a[0]
            self.__max_heapify(i, 0)
        return self.__a

    def get_a(self):
        return self.__a
