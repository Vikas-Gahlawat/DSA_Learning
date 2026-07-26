def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i], i
        i += 1
    return False

linear_search([2, 1, 5, 3, 6], 5)