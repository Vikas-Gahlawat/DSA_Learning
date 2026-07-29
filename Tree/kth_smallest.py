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
    
count = 0

def kth_smallest(node, k):
    global count
    if node is None:
        return None
    answer = kth_smallest(node.left, k)
    if answer is not None:
        return answer
    count += 1
    if count == k:
        return node.value
    answer = kth_smallest(node.right, k)
    return answer

kth_smallest(root, 2)    