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

diameter = 0

def diameter_of_bst(node):
    global diameter
    if node is None:
        return 0
    left = diameter_of_bst(node.left)
    right = diameter_of_bst(node.right)
    diameter = max(diameter, left + right)
    return 1 + max(left, right)
    
diameter_of_bst(root)
    