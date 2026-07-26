class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

head.next.next.next.next.next = head.next

def has_cyclic(head):
    if head is None:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False
    
has_cyclic(head)