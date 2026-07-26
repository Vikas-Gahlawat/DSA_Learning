def students_needed(books, students, capability):
    student = 1
    page = 0
    for book in books:
        if page + book <= capability:
            page += book
        else:
            page = book
            student += 1
    # At most 3 students may be used not Exactly 3 students must be used so we use <= not ==
    if student <= students:
        return True
    else:
        return False
    
def allocate_pages(books, students):
    if students > len(books):
        return -1
    left = max(books)
    right = sum(books)
    answer = 0
    while left <= right:
        mid = (right + left) // 2
        can_student = students_needed(books, students, mid)
        if can_student:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

allocate_pages([12,34,67,90], 2)
allocate_pages([10, 20, 30], 5)
            