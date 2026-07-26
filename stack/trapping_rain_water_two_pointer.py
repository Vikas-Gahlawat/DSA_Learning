def trapping_rain_water(heights):
    if not heights:
        return 0
    leftMax = heights[0]
    rightMax = heights[len(heights) - 1]
    left = 0
    right = len(heights) - 1
    water = 0
    while left < right:
        if leftMax <= rightMax:
            water += leftMax - heights[left]
            left += 1
            leftMax = max(leftMax, heights[left])
        else:
            water += rightMax - heights[right]
            right -= 1
            rightMax = max(rightMax, heights[right])
    return water
        
    