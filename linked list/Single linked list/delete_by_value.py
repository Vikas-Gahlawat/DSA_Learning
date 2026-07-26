class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

def delete_by_value(head, value):
    if head is None:
        return None
    if head.value == value:
        head = head.next
        return head
    
    current = head
    previous = head             #we can use previous = None becuase we are taking one before so for 1st it is None
    while current:
        if current.value == value:
            previous.next = current.next
            return head
        else:
            previous = current
            current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next
    
head = delete_by_value(head, 30)
    
print_linked_list(head)