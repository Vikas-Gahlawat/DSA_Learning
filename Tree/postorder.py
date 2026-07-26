class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value)

post_order(root)
