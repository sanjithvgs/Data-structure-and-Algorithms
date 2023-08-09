def solve(A):
    stack = []
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in A:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return 0
    if stack==[]:
      return 1
    return 0

A = "([{])}"
if solve(A):
  print("Paranthesis are proper")
else:
  print("Paranthesis not proper")

# output:
# Paranthesis not proper