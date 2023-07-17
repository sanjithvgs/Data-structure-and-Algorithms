class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def solve(A):
        if A.next==None:
            print(A.value,end=" ")
            print()
            return
        
        prev=None
        rh=A.next

        while A!=None:
            A.next=prev
            prev=A
            A=rh
            if rh!=None:
                rh=rh.next

        current=prev
        while current!=None:
            print(current.value,end=" ")
            current=current.next
        print()


# Creating a linked list
head = Node(1)
node2 = Node(7)
node3 = Node(5)

head.next = node2
node2.next = node3

# Passing the head to the solve function
solve(head)

# output:
# 5 7 1 