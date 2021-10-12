def insertionsort(a):
 for j in range(len(a)-1):
  i=j
  j=j+1
  key=a[j]
  while i>-1 and a[i]>key:
   a[i+1]=a[i]
   i=i-1
   a[i+1]=key
 return a
 

  
