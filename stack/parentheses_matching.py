def parentheses_matching(str):
    if len(str) == 0:
        return True
    stack = []
    for brace in str:
        if brace in '([{':
            stack.append(brace)
        if brace in ')]}':
            if brace == ")" and stack[-1] == "(":
                stack.pop()
            elif brace == "]" and stack[-1] == "[":
                stack.pop()
            elif brace == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
    
parentheses_matching("((((")


# an another optimised way or better way where we need not to use many if else
# def parentheses_matching(s):
#     stack = []
#     pairs = {
#         ')' : '(',
#         ']' : '[',
#         '}' : '{',
#     }
#     for brace in s:
#         if brace in '([{':
#             stack.append(brace)
#         elif brace in ')]}':
#             if not stack:
#                 return False
#             if stack[-1] != pairs[brace]:
#                 return False
#             stack.pop()
#     return len(stack) == 0