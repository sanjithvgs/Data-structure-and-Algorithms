A=list(map(int,input("Enter a list values to sort: ").split()))
n=len(A)
for i in range(n-1):
    for j in range(n-i-1):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]

print(A)

# output:
# Enter a list values to sort: 8 5 4 9 7 2 10
# [2, 4, 5, 7, 8, 9, 10]