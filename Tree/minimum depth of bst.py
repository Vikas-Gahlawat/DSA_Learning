class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)

def min_depth(node):
    if node is None:
        return 0
    queue = [node]
    depth = 1
    while queue:
        level_size = len(queue)
        while level_size:
            if queue[0].left is None and queue[0].right is None:
                return depth
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            queue.pop(0)
            level_size -= 1
        depth += 1
    return depth
    
min_depth(root)