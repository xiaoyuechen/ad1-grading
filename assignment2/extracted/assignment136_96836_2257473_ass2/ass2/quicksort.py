import array

def partition(a,p,r):
	x = a[r]
	i = p-1
	for j in range(p,r):
		if a[j] <= x:
			i+=1
			a[i],a[j] = a[j],a[i]
	a[i+1],a[r] = a[r],a[i+1]
	return i+1

def	recursivequicksort(a,p,r):
	if p<r:
		q= partition(a, p,r)
		recursivequicksort(a, p, q-1)
		recursivequicksort(a, q+1, r)

def quicksort(a):
	recursivequicksort(a,0,len(a)-1)