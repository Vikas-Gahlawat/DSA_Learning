class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

head = None

def merge_two_sorted_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.value <= head2.value:
        head, tail = head1, head1
        head1 = head1.next
    else:
        head, tail = head2, head2
        head2 = head2.next
    while head1 and head2:
        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next
            tail = tail.next
        else:
            tail.next = head2
            head2 = head2.next
            tail = tail.next
    if head1:
        tail.next = head1
    else:
        tail.next = head2
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next
   
head = merge_two_sorted_lists(head1, head2)

print_linked_list(head)
