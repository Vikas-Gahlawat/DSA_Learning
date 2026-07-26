# if element found in the array then return its index else return the index where the element should be inserted so that the array remain sorted

def search_insert_position(arr, target):
    left, right, answer = 0, len(arr) - 1, len(arr)
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

search_insert_position([2, 5, 8, 12, 16], 20)