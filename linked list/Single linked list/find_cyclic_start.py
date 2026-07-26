class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

head.next.next.next.next.next = head.next.next

def find_cycle_start(head):
    if head is None:
        return None
    slow = head
    fast = head
    # Step 1: Detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No cycle
        return None
    # Step 2: Find start of cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow 

start = find_cycle_start(head)

if start:
    print("Cycle starts at:", start.value)
else:
    print("No cycle")