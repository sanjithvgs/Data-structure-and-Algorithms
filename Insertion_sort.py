n=int(input("Enter the length of list/Array: "))  #Insertion Sort
lst=[]
print("Enter list/Array with space: ")
lst = list(map(int, input().split()))
for i in range(1,n):
    value=lst[i]
    index=i
    while (index>0 and lst[index-1]>value):
        lst[index]=lst[index-1]
        lst[index-1]=value
        index-=1
print("Insertion Sort: ",lst)
