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

def insert_bst(root, value):
    if root is None:
        root = Node(value)
        return root
    parent = root
    current = root
    # i write my own code and write this i am making parent and current equal at the end on the basic of that the current should be not none
    # as current move left and right it will become None and i don't want parent to be none so while moving when current become None don't
    # make parent to be none so i write this but there should be a better solution which is written below
    # while current:
    #     if parent.value <= value:
    #         current = current.right
    #     else:
    #         current = current.left
    #     if current:
    #         parent = current
    
    # we make parent = current at the loop start and then move current so when current become None nothing happen because
    # parent become current when it is valid so we can write 
    while current:
        parent = current
        if current.value <= value:
            current = current.right
        else:
            current = current.left
    if parent.value <= value:
        parent.right = Node(value)
    else:
        parent.left = Node(value)
    return root            
        
root = insert_bst(root, 65)