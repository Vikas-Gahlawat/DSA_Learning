class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

def middle_node(head):
    if head is None:
        return None
    slow = head
    fast = head    # if i use head.next like pointing fast a node after slow then no need to change codition
    while fast.next and fast.next.next:   #if we are not chaging fast pointer then have to change condition: while fast.next and fast.next.next
        slow = slow.next
        fast = fast.next.next
    return slow
    
def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next
    
middle_node(head)