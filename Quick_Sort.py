# Quick Sort

def partition(lst,s,e):
  pivot=lst[e]
  i=s-1
  for j in range(s,e):
    if lst[j]<pivot:
      i+=1
      lst[i],lst[j]=lst[j],lst[i]

  lst[e],lst[i+1]=lst[i+1],lst[e]
  return i+1

def quick_sort(lst,s,e):
  if s>=e:
    return
  p=partition(lst,s,e)
  quick_sort(lst,s,p-1)
  quick_sort(lst,p+1,e)


lst=[4,6,1,9,2,7,-3,0,1]
quick_sort(lst,0,len(lst)-1)
print("The sorted list: ",lst)

output:
[-3, 0, 1, 1, 2, 4, 6, 7, 9]