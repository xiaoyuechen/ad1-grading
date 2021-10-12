def quicksort(a,p,r):
 if p<r:
  q=partition(a,p,r)
  quicksort(a,p,q-1)
  quicksort(a,q+1,r)
 return a





def partition(a,p,r):
 x=a[r]
 i=p-1
 for j in range(p,r):
     if a[j]<=x:
         i+=1
         swap(a,i,j)
 swap(a,i+1,r)
 return i+1

















def swap(a, i, j):
 t = a[j]

 a[j] = a[i]
 a[i] = t
