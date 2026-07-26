# Hints:
#     Traverse left → right.
#     Store (price, index) in the stack.
#     While the top price is <= current price, pop it.
#     If the stack is empty:
#     span = current_index + 1
#     Otherwise:
#     span = current_index - previous_greater_index
#     Push the current (price, index)
# prices = [100, 80, 60, 70, 60, 75, 85]
# output = [1, 1, 1, 2, 1, 4, 6]

def stock_span(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while len(stack) > 0 and stack[-1][0] <= prices[i]:
            stack.pop()
        if not stack:
            answer[i] = i + 1
        else:
            answer[i] = i - stack[-1][1]
        stack.append((prices[i], i))
    return answer

stock_span([100, 80, 60, 70, 60, 75, 85])