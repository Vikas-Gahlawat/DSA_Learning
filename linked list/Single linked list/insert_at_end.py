class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

head = a
a.next = b
b.next = c
c.next = d

def insert_at_end(head, value):
    if head is None:
        return Node(value)
    current = head
    while current.next:
        current = current.next
    current.next = Node(value)
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next

head = insert_at_end(head, 50)

print_linked_list(head)

