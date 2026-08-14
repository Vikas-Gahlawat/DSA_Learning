class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None
        
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)

def path_sum(node, target):
    if node is None:
        return False
    target -= node.value
    if node.left is None and node.right is None:
        return target == 0
    left = path_sum(node.left, target)
    right = path_sum(node.right, target)
    return left or right
    
path_sum(root, 22)



# the more efficient solution when there is no need to get left and right extra variable and work
# def path_sum(node, target):
#     if node is None:
#         return False
#     target -= node.value
#     if node.left is None and node.right is None:
#         return target == 0
#     return (
#         path_sum(node.left, target) or
#         path_sum(node.right, target)
#     )
# just pass both recursion in the return statement 