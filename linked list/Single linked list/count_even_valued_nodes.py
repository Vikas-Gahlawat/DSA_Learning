class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

a = Node(10)
b = Node(21)
c = Node(30)
d = Node(41)
e = Node(50)

head = a
a.next = b
b.next = c
c.next = d
d.next = e

def count_even_valued_nodes(head):
    even_counter = 0
    node = head
    while node:
        if node.value % 2 == 0:
            even_counter += 1
        node = node.next
    return even_counter

count_even_valued_nodes(head)