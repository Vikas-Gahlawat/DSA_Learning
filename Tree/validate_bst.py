class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

root = Node(40)
root.left = Node(20)
root.right = Node(60)
root.left.left = Node(10)
root.left.right = Node(50)

pos_inf = float('inf')
neg_inf = float('-inf')

def is_valid_bst(node, minimum, maximum):
    # Base case: an empty node is a valid BST
    if node is None:
        return True
    # Check if the current node's value violates the min/max constraints
    if not (minimum < node.value < maximum):
        return False
    # Recursively validate the left and right subtrees with updated bounds
    left = is_valid_bst(node.left, minimum, node.value)
    right = is_valid_bst(node.right, node.value, maximum)
    
    return left and right

is_valid_bst(root, neg_inf, pos_inf)



# Another popular way to solve this is by using the property of an In-Order Traversal (Left -> Root -> Right).If you do an in-order traversal on a valid Binary Search Tree, the values must always be in strictly ascending order. You can track the previously visited node and ensure each current node is larger than the last.

# def is_valid_bst_inorder(root):
#     prev = float('-inf')
    
#     def inorder(node):
#         nonlocal prev
#         if not node:
#             return True
        
#         # Check left subtree
#         if not inorder(node.left):
#             return False
        
#         # Current node must be greater than the previous node
#         if node.value <= prev:
#             return False
#         prev = node.value
        
#         # Check right subtree
#         return inorder(node.right)
        
#     return inorder(root)
