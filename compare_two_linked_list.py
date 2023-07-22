class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Create the first linked list: 1 -> 2 -> 3
list1_values = [1, 2, 3]
head1 = create_linked_list(list1_values)

# Create the second linked list: 4 -> 5 -> 6
list2_values = [4, 5, 6]
head2 = create_linked_list(list2_values)

# Return the heads of both linked lists
def get_linked_list_heads():
    return head1, head2

#compare code
def solve(A,B):
  curr_A=A
  curr_B=B
  while curr_A!=None and curr_B!=None:
      if curr_A.value==curr_B.value:
          curr_A=curr_A.next
          curr_B=curr_B.next
      else:
          return 0
  return 1


# Test the function by printing the heads of both linked lists
head1, head2 = get_linked_list_heads()
print(solve(head1,head2))
