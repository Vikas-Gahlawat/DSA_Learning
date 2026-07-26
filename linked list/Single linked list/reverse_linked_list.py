class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

def reverse_linked_list(head):
    if head is None:
        return None
    current = head
    previous = None
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next
    
head = reverse_linked_list(head)
    
print_linked_list(head)