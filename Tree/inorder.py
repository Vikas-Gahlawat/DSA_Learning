class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)

in_order(root)
