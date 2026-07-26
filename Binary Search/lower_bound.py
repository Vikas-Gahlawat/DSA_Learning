# First element greater than or equal to the target.

def lower_bound(arr, target):
    left, right, answer = 0, len(arr) - 1, -1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

lower_bound([2, 5, 8, 12, 16], 10)
lower_bound([2,5,5,5,8], 5)