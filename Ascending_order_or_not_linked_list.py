class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def solve(A):
  curr_node=A
  if curr_node.next==None:
      return 1
  while curr_node.next!=None:
      if curr_node.val>curr_node.next.val:
          return 0
      curr_node=curr_node.next
  return 1


# Creating a linked list
head = Node(1)
node2 = Node(4)
node3 = Node(5)

head.next = node2
node2.next = node3

# Passing the head to the solve function
print(solve(head))

# output:
# 1