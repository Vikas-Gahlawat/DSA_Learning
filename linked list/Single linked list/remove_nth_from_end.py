class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def remove_nth_from_end(head, n):
    slow = head
    fast = head
    for i in range(n + 1):
        if fast is None:
            print("please enter the valid nth node from the end")
            return head
        fast = fast.next
    if fast is None:
        head = head.next
        return head
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
    
head = remove_nth_from_end(head, 2)
