class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)
root.right.left.right = Node(65)

def check_height(node):
    if node is None:
        return 0
    left = check_height(node.left)
    if left == -1:
        return -1
    right = check_height(node.right)
    if right == -1:
        return -1
    diff = abs(left - right)
    if diff > 1:
        return -1
    return 1 + max(left, right)
    
def is_balanced(node):
    return check_height(node) != -1

is_balanced(root)
    