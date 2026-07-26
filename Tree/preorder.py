class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

def pre_order(root):
    if root is None:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)

pre_order(root)
