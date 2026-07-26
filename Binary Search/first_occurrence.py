def first_occurrence(arr, target):
    left, right, answer = 0, len(arr) - 1, -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    return answer

first_occurrence([2,4,4,4,7,9,12], 4)