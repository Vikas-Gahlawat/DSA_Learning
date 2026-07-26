class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def reverse_linked_list_2(head, left, right):
    sorted_tail = None
    rev_tail = head
    for i in range(left - 1):
        sorted_tail = rev_tail
        rev_tail = rev_tail.next
    current = rev_tail
    previous = None
    for i in range(right - left + 1):
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    sorted_tail.next = previous
    rev_tail.next = current
    return head
            
head = reverse_linked_list_2(head, 2, 4)



# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

# def reverse_linked_list_2(head, left, right):
#     sorted_tail = None
#     rev_tail = head

#     # Move rev_tail to the left-th node
#     for _ in range(left - 1):
#         sorted_tail = rev_tail
#         rev_tail = rev_tail.next

#     # Reverse the sublist
#     current = rev_tail
#     previous = None

#     for _ in range(right - left + 1):
#         next_node = current.next
#         current.next = previous
#         previous = current
#         current = next_node

#     # Connect the first part
#     if sorted_tail:
#         sorted_tail.next = previous
#     else:
#         head = previous

#     # Connect the last part
#     rev_tail.next = current

#     return head