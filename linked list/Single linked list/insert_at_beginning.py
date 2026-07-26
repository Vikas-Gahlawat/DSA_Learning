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

def insert_at_beginning(head, value):
    newNode = Node(value)
    newNode.next = head
    head = newNode
    return head
    
def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next
        
head = insert_at_beginning(head, 5)

print_linked_list(head)