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

def lowest_common_ancestor(root, p, q):
    current = root
    
    while current:        
        if current.value > p and current.value > q:
            current = current.left
        elif current.value < p and current.value < q:
            current = current.right
        else:
            return current.value        
    return None
    
lowest_common_ancestor(root, 20, 40)