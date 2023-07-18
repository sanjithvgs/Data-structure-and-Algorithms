class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def solve(A):
    slow=A
    fast=A

    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next

    return slow.val


# Creating a linked list
head = Node(1)
node2 = Node(7)
node3 = Node(5)

head.next = node2
node2.next = node3

# Passing the head to the solve function
print("Middle element is:",solve(head))

# output:
# Middle element is: 7