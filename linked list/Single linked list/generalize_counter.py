class Node:
    def __init__(self, value):
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

def count_nodes_if(head, condition): #count, odd, even, positive, negative like conditions
    counter = 0
    current = head
    match condition:
        case "count":
            while current:
                counter += 1
                current = current.next
        case "odd":
            while current:
                if current.value % 2 != 0:
                    counter += 1
                current = current.next
        case "even":
            while current:
                if current.value % 2 == 0:
                    counter += 1
                current = current.next
        case "positive":
            while current:
                if current.value >= 0:
                    counter += 1
                current = current.next
        case "negative":
            while current:
                if current.value < 0:
                    counter += 1
                current = current.next
        case _:
            return print("enter the correct condition from count, odd, even, positive, negative")
    return counter

count_nodes_if(head, "count")
        