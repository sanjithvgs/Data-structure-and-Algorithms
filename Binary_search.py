n=int(input("Enter the length of list/Array: "))  #Binary search using low, high and mid
lst=[]
print("Enter sorted list/Array with space: ")
lst = list(map(int, input().split()))
find=int(input("Enter element to search: "))
low=0
high=n-1
while (low<=high):
    mid=int(low+((high-low)/2))
    if lst[mid]>find:
        high=mid-1
    elif lst[mid]<find:
        low=mid+1
    else:
        print("Element found at index: ",mid)
        break
if low>high:
    print('Not found')
