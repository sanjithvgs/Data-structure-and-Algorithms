class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def solve(head,target):
    current = head
    while current is not None:
        if current.value==target:
            return "Found"
        current = current.next
    return "Not Found"


# Creating a linked list
head = Node(1)
node2 = Node(7)
node3 = Node(5)

head.next = node2
node2.next = node3

# Passing the head to the solve function
print(solve(head,target=7))

# output:
# Found