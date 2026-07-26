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

def search_bst(root, target):
    if root is None or root.value == target:
        return root

    if target < root.value:
        return search_bst(root.left, target)

    return search_bst(root.right, target)

search_bst(root, 60)