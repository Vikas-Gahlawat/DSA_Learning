class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None
        
# you can write this becuase we are not taking any extra varible we are doing everything clean with help of head and define everything with head
        
# head = Node(1)
# head.next = Node(2)
# head.next.prev = head
# head.next.next = Node(3)
# head.next.next.prev = head.next
# head.next.next.next = Node(4)
# head.next.next.next.prev = head.next.next
# head.next.next.next.next = head
# head.prev = head.next.next.next

# you can write this also so that it is a little easy for us to determine what is next and previous
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

head = a
a.prev = d
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
d.next = a