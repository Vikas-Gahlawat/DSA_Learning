def left_max(height):
    left = [0] * len(height)
    current = 0
    for i in range(len(height)):
        current = max(current, height[i])
        left[i] = current
    return left

def right_max(height):
    right = [0] * len(height)
    current = 0
    for i in range(len(height) - 1, -1, -1):
        current = max(current, height[i])
        right[i] = current
    return right

def trapping_rain_water(heights):
    water = 0
    prv = left_max(heights)
    nxt = right_max(heights)
    for i in range(len(heights)):
        water += min(prv[i], nxt[i]) - heights[i]
    return water

trapping_rain_water([3, 0, 2, 0, 4])