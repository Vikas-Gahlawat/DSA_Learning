class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

def middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_list(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def is_palindrome(head):
    if head is None and head.next is None:
        return True
    mid = middle_node(head)
    reverse_head = reverse_list(mid)
    
    first = head
    second = reverse_head
    while second:
        if first.value != second.value:
            reverse_list(reverse_head)
            return False
        first = first.next
        second = second.next
    reverse_list(reverse_head)
    return True

is_palindrome(head)