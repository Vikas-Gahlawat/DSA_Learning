class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.right.right = Node(9)

def bfs(node):
    if node is None:
        return []
    answer = []
    level_number = 1
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
        if level_number % 2 == 0:
            level.reverse()
            answer.append(level)
        else:
            answer.append(level)
        level_number += 1
    return answer
    
bfs(root)


# another method with deque
from collections import deque
def level_order(root):
    if root is None:
        return []
    queue = deque([root])
    answer = []
    level_number = 1
    while queue:
        level = deque([])
        for _ in range(len(queue)):
            node = queue.popleft()
            if level_number % 2 == 0:
                level.appendleft(node.value)
            else:
                level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        answer.append(list(level))
        level_number += 1
    return answer

print(level_order(root))