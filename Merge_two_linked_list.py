class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def create_linked_list(values):
    if not values:
        return None

    root = Node(values[0])
    current = root

    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node
        current = new_node

    return root


# Create two linked lists with values [1, 2, 3] and [4, 5, 6]
list1_values = [1, 2, 3]
list2_values = [7, 8, 6]

list1_root = create_linked_list(list1_values)
list2_root = create_linked_list(list2_values)


#solve function

def solve(A,B):
  h=None
  t=None

  if A.val<B.val:
      h=A
      t=A
      A=A.next
  else:
      h=B
      t=B
      B=B.next
  while A!=None and B!=None:
      if A.val<B.val:
          t.next=A
          t=t.next
          A=A.next
      else:
          t.next=B
          t=t.next
          B=B.next
  if A!=None:
      t.next=A
  if B!=None:
      t.next=B
  return h

# Return the root nodes of both linked lists
root=solve(list1_root,list2_root)

#print linked list
current=root
while current:
  if current.next==None:
    print(current.val)
  else:
    print(current.val,"->",end="")
  current=current.next


# output:
# 1 ->2 ->3 ->7 ->8 ->6