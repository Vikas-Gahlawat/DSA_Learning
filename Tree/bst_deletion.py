# Calculating Time Complexity for Your Iterative Code
#     Let's look at your code's path 
#         when deleting a node:search_node: Uses a while loop to go down the tree from the root to the target node. In the worst case, this takes $\mathcal{O}(h)$ steps, where $h$ is the height of the tree.
#         inorder_successor (if it's a two-child deletion): Goes right once, then loops down the left branch all the way to the bottom. This also takes $\mathcal{O}(h)$ steps.
#         Deletion helpers (delete_leaf_node, delete_one_child_node): These only do a few direct pointer reassignment checks. They take constant time $\mathcal{O}(1)$.
#         Total Time Complexity:
#             $$\mathcal{O}(h) + \mathcal{O}(h) + \mathcal{O}(1) = \mathcal{O}(h)$$
# If the BST is balanced, the height $h = \log n$, making the time complexity $\mathcal{O}(\log n)$.
# If the BST is skewed (like a straight line/linked list), the height $h = n$, making the time complexity $\mathcal{O}(n)$.

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

# search of node which we have to delete make sure you can access parent node
def search_node(root, value):
    parent = None
    current = root
    while current:
        if current.value == value:
            return parent, current
        parent = current
        if value < current.value:
            current = current.left
        else:
            current = current.right
    return parent, current
    
# search of successor node when there are two child of node so that the BST follow its rule
def inorder_successor(current):
    successor_parent = current
    successor = current.right
    while successor.left:
        successor_parent = successor
        successor = successor.left
    return successor_parent, successor

# delete left node when the left and right both are None so we have to delete the leaf node
def delete_leaf_node(root, parent, current):
    if parent is None:
        root = None
        return root
    if parent.left == current:
        parent.left = None
    else:
        parent.right = None
    return root

# delete node having one child whether on the right or on the left
def delete_one_child_node(root, parent, current):
    if parent is None:
        if current.left is None:
            root = current.right
            return root
        else:
            root = current.left
            return root
    if parent.left == current:
        if current.right is None:
            parent.left = current.left
            return root
        parent.left = current.right
        return root
    else:
        if current.right is None:
            parent.right = current.left
            return root
        parent.right = current.right
        return root
        
# delete two child node when the node have two subtree so we have to find successor and replace then delete that successor also
def delete_two_child_node(root, current, value):
    successor_parent, successor = inorder_successor(current)
    current.value = successor.value
    if successor.left is None and successor.right is None:
        root = delete_leaf_node(root, successor_parent, successor)
    else:
        root = delete_one_child_node(root, successor_parent, successor)
    return root

# main delete node function which we call to delete any node from the BST tree
def delete_node(root, value):
    if root is None:
        return None
    parent, current = search_node(root, value)
    if current is None:
        return root
    elif current.left is None and current.right is None:
        root = delete_leaf_node(root, parent, current)
    elif (current.left is None and current.right) or (current.right is None and current.left):
    # elif current.left is None or current.right is None:
        root = delete_one_child_node(root, parent, current)
    else:
        root = delete_two_child_node(root, current, value)
    return root   
    
# call of the function to delete 50 from the BST
root = delete_node(root, 50)


# some cleaner program which i have to think but teacher teach me. my also working but i have to write a lot to do the same work
# def delete_one_child_node(root, parent, current):
#     # Determine which child 'current' has
#     child = current.left if current.left else current.right
    
#     if parent is None:
#         return child # This becomes the new root
    
#     if parent.left == current:
#         parent.left = child
#     else:
#         parent.right = child
#     return root

# recursive method to delete a node

# def delete_node(root, value):
#     if not root:
#         return None
#     # 1. Traverse to find the node
#     if value < root.value:
#         root.left = delete_node(root.left, value)
#     elif value > root.value:
#         root.right = delete_node(root.right, value)
#     else:
#         # 2. Node found! Handle the 3 cases:
#         # Case 1: Leaf node or only right child
#         if not root.left:
#             return root.right
#         # Case 2: Only left child
#         if not root.right:
#             return root.left
#         # Case 3: Two children
#         # Find inorder successor (min value in right subtree)
#         curr = root.right
#         while curr.left:
#             curr = curr.left
#         root.value = curr.value  # Copy value
#         root.right = delete_node(root.right, curr.value)  # Delete successor
#     return root

# What is the space complexity, and could you run into any issues with it?
# The space complexity is $\mathcal{O}(h)$ due to the call stack. If the tree becomes skewed and looks like a linked list, $h$ becomes $n$, which could risk a stack overflow. However, for a balanced tree, it's very efficient. For a reasonably balanced BST with $1,000,000$ elements, the height ($h$) is only about $\log_2(1,000,000) \approx 20$. A call stack depth of 20 frames takes up virtually zero memory.


# Your Code: $\mathcal{O}(h)$ time and $\mathcal{O}(1)$ space.
# The Recursive Code: $\mathcal{O}(h)$ time and $\mathcal{O}(h)$ space (due to the call stack).