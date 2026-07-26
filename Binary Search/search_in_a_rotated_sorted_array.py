def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1
    # it break the array in half and again and again check the left is sorted or right is sorted
    # and in sorted protion check target if it is found then search in it by moving pointer else in other portion
    # if not in sorted portion then again and agian loop continue until the condition and check left and right
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            # left sorted, then check target in left sorted array
            if arr[left] <= target < arr[mid]:
                # if found then move right pointer and then search the target
                right = mid -1
            else:
                # else move the left pointer and then search the target
                left = mid + 1
        else:
            # right sorted, then check target in the right sorted array
            if arr[mid] < target <= arr[right]:
                # if found then move left pointer to right side and search the target
                left = mid + 1
            else:
                # else move right pointer and search the target
                right = mid - 1
    return -1
search_rotated([4, 6, 7, 8, 9, 0, 1], 9)