from collections import deque
def solve(A):
    stack=deque()
    stack.append(A[0])    
    for ind in range(1,len(A)):
        if len(stack)>0 and A[ind]==stack[-1]:
            stack.pop()
        else:
            stack.append(A[ind])
    result=""
    for val in stack:
        result+=val
    return result

A = "abccbc"
print(solve(A))

# output:
# ac


#Explanation::
# The Given string is "abccbc".

# Remove the first occurrence of consecutive identical pairs of characters "cc".
# After removing the string will be "abbc".

# Again Removing the first occurrence of consecutive identical pairs of characters "bb".
# After remvoing, the string will be "ac".

# Now, there is no consecutive identical pairs of characters.
# Therefore the string after this operation will be "ac".