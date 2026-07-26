class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def remove_nth_from_end_with_dummy(head, n):
    dummy = Node(0)
    dummy.next = head
    
    slow = dummy
    fast = dummy
    for i in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
    
head = remove_nth_from_end_with_dummy(head, 2)
