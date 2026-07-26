class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

def delete_last(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    previous = head
    while current.next:
        previous = current
        current = current.next
    previous.next = None
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next

head = delete_last(head)

print_linked_list(head)