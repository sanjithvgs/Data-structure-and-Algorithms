# Merge sort

def merge(a,s,m,e):
  c=[0]*(e-s+1)
  p1=s
  p2=m+1
  k=0

  while p1<=m and p2<=e:
    if a[p1]<a[p2]:
      c[k]=a[p1]
      p1+=1
      k+=1
    else:
      c[k]=a[p2]
      p2+=1
      k+=1

  while p1<=m:
    c[k]=a[p1]
    p1+=1
    k+=1

  while p2<=e:
    c[k]=a[p2]
    p2+=1
    k+=1

  for i in range(len(c)):
    A[i+s]=c[i]

def merge_sort(A,s,e):
  if s==e:
    return
  m=(s+e)//2
  merge_sort(A,s,m)
  merge_sort(A,m+1,e)

  merge(A,s,m,e)
  return A

A=[4,6,1,9,2,7,-3,0,1]
print(merge_sort(A,0,len(A)-1))

# output:
# [-3, 0, 1, 1, 2, 4, 6, 7, 9]