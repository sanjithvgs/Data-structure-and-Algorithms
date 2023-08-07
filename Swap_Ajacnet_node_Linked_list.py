def swapPairs(A):
    if A is None or A.next is None:
        return A
    prev=None
    curr=A
    nextt=A.next
    while curr and nextt:
        curr.next=nextt.next
        nextt.next=curr
        if prev==None:
            A=nextt
        else:
            prev.next=nextt
        prev=curr
        curr=curr.next
        if curr==None:
            break
        nextt=curr.next
    return A


#Create Linked list start
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        current.next = new_node
        current = new_node

    return head

#Create Linked list end


A = [1, 2, 3, 4]
head = create_linked_list(A)
new_head=swapPairs(head)

current=new_head
while current:
  print(current.val,end=" ")
  current=current.next

# output:
# 2 1 4 3 

# (1, 2) and (3, 4) are the adjacent nodes. Swapping them will result in 2 -> 1 -> 4 -> 3