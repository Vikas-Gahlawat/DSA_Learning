# binary search only work with sorted array if array is not sorted then we can't use binary search
# Use the list.sort() method if you do not need to keep the original, unsorted version of your data like arr.sort()
# Use the built-in Python sorted() function if you want to leave the original list untouched like new_arr = sorted(arr)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2       #you can calculate mid as also left + (right - left) // 2 because it's overflow-safe in languages like Java and C++
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
            
    
binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9)