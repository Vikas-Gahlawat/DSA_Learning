def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (right + left) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle -1
    return -1

binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 50)