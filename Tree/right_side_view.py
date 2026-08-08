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

def right_side_view(node):
    # need to code for later
    ...
    
right_side_view(root)