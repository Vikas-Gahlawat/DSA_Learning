# My approach:
    # Build prev[]
    # Build next[]
    # Compute areas
    # Time: O(n)
    # Space: O(n) for prev + next + stack

def previous_smaller_index(heights):
    stack = []
    ans = [-1] * len(heights)
    for i in range(len(heights)):
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((heights[i], i))
    return ans
    
def next_smaller_index(heights):
    stack = []
    ans = [len(heights)] * len(heights)
    for i in range(len(heights) - 1, -1, -1):
        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1][1]
        stack.append((heights[i], i))
    return ans

def largest_rectangle_area(heights):
    prev = previous_smaller_index(heights)
    nxt = next_smaller_index(heights)
    maximum = 0
    for i in range(len(heights)):
        width = nxt[i] - prev[i] - 1
        maximum = max(width * heights[i], maximum)
    return maximum

largest_rectangle_area([2, 1, 5, 6, 2, 3])

# The interview-preferred solution computes the area on the fly while maintaining a monotonic increasing stack, so there's no need to explicitly store previous and next smaller indices.
# Idea

# Maintain a stack of indices whose heights are in increasing order.

# When you encounter a bar shorter than the top of the stack:

# The taller bar on top can no longer extend to the right.
# So you immediately compute its maximum rectangle.
# The current index is its next smaller.
# The new stack top (after popping) is its previous smaller.

# Thus, both boundaries are known at the moment you pop.

# def largest_rectangle_area(heights):
#     stack = []
#     maximum = 0
#     n = len(heights)
#     for i in range(n + 1):
#         curr_height = 0 if i == n else heights[i]
#         while stack and heights[stack[-1]] > curr_height:
#             h = heights[stack.pop()]
#             if stack:
#                 width = i - stack[-1] - 1
#             else:
#                 width = i
#             maximum = max(maximum, h * width)
#         stack.append(i)
#     return maximum