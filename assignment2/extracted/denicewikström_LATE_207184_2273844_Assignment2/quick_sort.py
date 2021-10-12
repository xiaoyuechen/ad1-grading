import sys

class quicksort:

    def __init__(self, a):
        self.__a = a.copy()
        self.__a = self.__sort(0, len(self.__a)-1)

    def __partition(self, start, stop):
        x = self.__a[stop]
        i = start - 1
        for j in range(start, stop):
            if self.__a[j] <= x:
                i = i+1
                # exchange
                temp = self.__a[i]
                self.__a[i] = self.__a[j]
                self.__a[j] = temp
        # exchange
        temp = self.__a[i+1]
        self.__a[i+1] = self.__a[stop]
        self.__a[stop] = temp
        return i+1

    def __sort(self, start, stop):
        if start < stop:
            q = self.__partition(start, stop)
            self.__sort(start, q-1)
            self.__sort(q+1, stop)
        return self.__a

    def get_a(self):
        return self.__a
