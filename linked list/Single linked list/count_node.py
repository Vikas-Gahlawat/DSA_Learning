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

def count_nodes(head):
    counter = 0
    node = head
    while node:
        counter += 1
        node = node.next
    return counter

count_nodes(head)