def Max_Heapify(lista, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lista[i] < lista[left]:
        largest = left

    if right < n and lista[largest] < lista[right]:
        largest = right

    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        Max_Heapify(lista, n, largest)

def Heapsort(lista):
    n = len(lista)

    #Build_Max_Heap
    for i in range(n // 2 - 1, -1, -1):
        Max_Heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        Max_Heapify(lista, i, 0)
    return lista

lista = [ 14, 5, 7, 8, 22, 19, 2]
Heapsort(lista)
print("The lista is: ", lista)

L = Heapsort(lista)

f = open("Heapsort.txt", "w+")
for i in L:
    f.writelines("%s\n" % i)
f.close()