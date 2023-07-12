# A=>Root
# B=>Value
# C=>position
def solve(A, B, C):
    current=A
    new_node=ListNode(B)
    if C==0:
        new_node.next=current
        return node
    while C!=1 and current.next!=None:
        C-=1
        current=current.next
    new_node.next=current.next
    current.next=new_node
    return A

A = 1 -> 2
B = 3
C = 0
solve(A,B,C)

# output:
# 3 -> 1 -> 2