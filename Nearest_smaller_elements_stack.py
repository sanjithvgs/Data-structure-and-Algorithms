def nearest_smaller_elements(arr):
    n = len(arr)
    result = [-1] * n  # Initialize the result array with -1
    stack = []  # Initialize an empty stack to store indices
    
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()  # Pop elements from the stack while they are greater than or equal to the current element
        if stack:
            result[i] = arr[stack[-1]]  # Set the result with the nearest smaller element
        stack.append(i)  # Push the current index onto the stack
    
    return result


A = [4, 5, 2, 10, 8]
result = nearest_smaller_elements(A)
print(result)  


# Output: [-1, 4, -1, 2, 2]
