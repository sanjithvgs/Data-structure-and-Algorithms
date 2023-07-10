# A is head of linked list
def solve(A):
    current=A
    while current!=None:
        print(current.val,end=" ")
        current=current.next
    print()

solve(A)