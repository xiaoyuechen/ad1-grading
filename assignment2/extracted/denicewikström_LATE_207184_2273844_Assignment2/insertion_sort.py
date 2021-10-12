import sys

class inssort:

    def __init__(self, a):
        self.__a = a.copy()
        self.__a = self.__sort()

    def __sort(self):
        for j in range(1, len(self.__a)):
            key = self.__a[j]

            i = j-1

            while i >= 0 and self.__a[i] > key:
                self.__a[i+1] = self.__a[i]
                i = i-1

            self.__a[i+1] = key

        return self.__a

    def get_a(self):
        return self.__a
