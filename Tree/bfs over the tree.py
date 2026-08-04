class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(60)

    
def level_order(node):
    if node is None:
        return []
    answer = []
    queue = [node]
    while queue:
        level_size = len(queue)
        level = []
        while level_size:
            level.append(queue[0].value)
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
            level_size -= 1
        answer.append(level)
    return answer
    
print(level_order(root))


# Even better (using deque)
# Using pop(0) on a list is O(n). A deque is more efficient:
# from collections import deque
# def level_order(root):
#     if root is None:
#         return []
#     queue = deque([root])
#     answer = []
#     while queue:
#         level = []
#         for _ in range(len(queue)):
#             node = queue.popleft()
#             level.append(node.value)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         answer.append(level)
#     return answer

# print(level_order(root))