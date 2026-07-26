class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

def delete_first(head):
    if head is None:
        return None
    head = head.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next

head = delete_first(head)

print_linked_list(head)