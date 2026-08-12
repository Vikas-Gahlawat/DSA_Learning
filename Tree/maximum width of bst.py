class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.right.right = Node(50)

def max_width(node):
    if node is None:
        return 0
    queue = [[node, 0]]
    width = 0
    while queue:
        level_size = len(queue)
        width = max(width, queue[len(queue) - 1][1] - queue[0][1] + 1)
        for i in range(level_size):
            if queue[0][0].left:
                queue.append([queue[0][0].left, (2 * queue[0][1]) + 1])
            if queue[0][0].right:
                queue.append([queue[0][0].right, (2 * queue[0][1]) + 2])
            queue.pop(0)
    return width
    
max_width(root)

# optimization for this code which i have to use and learn
# from collections import deque
# queue = deque([(node,0)])
# current, index = queue.popleft()

# 2. another is don't repid use queue[0][1]
# current, index = queue.pop(0)
# current.left
# current.right
# index

# 3. 

# clean and easy to understand code which i don't think so it is suggested code for later learning and understanding
# def max_width(node):
#     if node is None:
#         return 0
#     queue = [[node, 0]]
#     max_width = 0
#     while queue:
#         level_size = len(queue)
#         first_index = queue[0][1]
#         last_index = queue[level_size - 1][1]
#         max_width = max(max_width, last_index - first_index + 1)
#         for _ in range(level_size):
#             current, index = queue.pop(0)
#             if current.left:
#                 queue.append([current.left, 2 * index + 1])
#             if current.right:
#                 queue.append([current.right, 2 * index + 2])
#     return max_width