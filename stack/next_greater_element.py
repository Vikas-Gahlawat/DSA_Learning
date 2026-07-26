# Traverse from right to left.
# Maintain a stack.
# Pop all smaller or equal elements.
# If the stack is empty → answer is -1.
# Otherwise → answer is stack[-1].
# Push the current element.

def next_greater_number(arr):
    stack = []
    current = 0
    for index in range(len(arr) - 1 , -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[index]:
            stack.pop()
        if len(stack) == 0:
            current = arr[index]
            arr[index] = -1
        else:
            current = arr[index]
            arr[index] = stack[-1]
        stack.append(current)
    return arr
        
next_greater_number([1, 3, 2, 4])


# optimized way online is given below
# def next_greater_number(arr):
#     stack = []
#     for i in range(len(arr) - 1, -1, -1):
#         while stack and stack[-1] <= arr[i]:
#             stack.pop()
#         if not stack:
#             answer = -1
#         else:
#             answer = stack[-1]
#         stack.append(arr[i])
#         arr[i] = answer
#     return arr
# next_greater_number([1, 3, 2, 4])