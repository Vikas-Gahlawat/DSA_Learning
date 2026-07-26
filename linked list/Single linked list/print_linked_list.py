class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)

head = a
a.next = b
b.next = c

def print_linked_list(header):
    node = header
    while node:
        print(node.value)
        node = node.next
        
print_linked_list(head)