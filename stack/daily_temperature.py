def daily_temperature(arr):
    stack = []
    answer = 0
    for i in range(len(arr) -1, -1, -1):
        while len(stack) > 0 and stack[-1]['value'] <= arr[i]:
            stack.pop()
        if not stack:
            stack.append({'value':arr[i], 'index':i})
            arr[i] = answer
        else:
            answer = stack[-1]['index']
            stack.append({'value':arr[i], 'index':i})
            arr[i] = answer - i
    return arr

daily_temperature([73, 74, 75, 71, 69, 72, 76, 73])

# optimised way or easy to read 
# def daily_temperatures(arr):
#     stack=[]
#     ans=[0]*len(arr)
#     for i in range(len(arr)-1,-1,-1):
#         while stack and stack[-1][0]<=arr[i]:
#             stack.pop()
#         if stack:
#             ans[i]=stack[-1][1]-i
#         stack.append((arr[i],i))
#     return ans