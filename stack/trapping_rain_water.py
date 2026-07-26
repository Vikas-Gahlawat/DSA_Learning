def leftMax(heights):
    stack = []
    ans = [0] * len(heights)
    for i in range(len(heights)):
        while stack and stack[-1] <= heights[i]:
            stack.pop()
        if not stack:
            stack.append(heights[i])
            ans[i] = stack[-1]
        else:
            ans[i] = stack[-1]
            if stack[-1] < heights[i]:
                stack.append(heights[i])
    return ans     
    
def rightMax(heights):
    stack = []
    ans = [0] * len(heights)
    for i in range(len(heights) - 1, -1, -1):
        while stack and stack[-1] <= heights[i]:
            stack.pop()
        if not stack:
            stack.append(heights[i])
            ans[i] = stack[-1]
        else:
            ans[i] = stack[-1]
            if stack[-1] < heights[i]:
                stack.append(heights[i])
    return ans
    
def trapping_rain_water(heights):
    water = 0
    prv = leftMax(heights)
    nxt = rightMax(heights)
    for i in range(len(heights)):
        water += min(prv[i], nxt[i]) - heights[i]
    return water

trapping_rain_water([3, 0, 2, 0, 4])