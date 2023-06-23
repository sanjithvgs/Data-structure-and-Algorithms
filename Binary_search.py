# Binary search

lst=[-3, 0, 1, 2, 4, 6, 7, 9]
low=0
high=len(lst)-1
k=4
flag=False
while low<=high:
  mid=(low+high)//2
  if lst[mid]==k:
    flag=True
    break
  if lst[mid]<k:
    low=mid+1
  else:
    high=mid-1

if flag:
  print("The index of that element is:",mid)
else:
  print("Element not exist")

# output:
# The index of that element is: 3