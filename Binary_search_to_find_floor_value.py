# Binary Search to find floor value

def search(lst,k):
  l=0
  r=len(lst)-1
  ans=-float('inf')

  while l<=r:
    mid=(l+r)//2

    if lst[mid]==k:
      return lst[mid]
    elif lst[mid]<k:
      ans=lst[mid]
      l=mid+1
    else:
      r=mid-1
  return ans


lst=[-3, 0, 1, 2, 4, 6, 7, 9]
print(search(lst,5))

# output:
# 4