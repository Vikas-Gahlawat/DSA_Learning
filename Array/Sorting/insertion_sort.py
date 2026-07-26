def insertion_sort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    for pass_num in range(1, length):
        key = arr[pass_num]
        j = pass_num - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    
insertion_sort([2, 5, 6, 1, 3, 4])


# def insertion_sort(arr):
#     """
#     Sorts a list in ascending order using the Insertion Sort algorithm.

#     Time Complexity:
#         Best Case : O(n)
#             -> Array is already sorted.
#             -> The while loop never shifts elements.

#         Average   : O(n²)

#         Worst     : O(n²)
#             -> Reverse sorted array.
#             -> Every new element must be shifted to the beginning.

#     Space Complexity:
#         O(1)
#             -> Sorting is done in-place.
#             -> No extra array is created.

#     Insertion Sort is a stable sorting algorithm.
#     Equal elements keep their original relative order.
#     """

#     # Store the length once instead of repeatedly calling len(arr).
#     length = len(arr)

#     # If the list has 0 or 1 element,
#     # it is already sorted.
#     if length <= 1:
#         return arr

#     # Start from index 1 because a single element
#     # (index 0) is already considered sorted.
#     #
#     # We will insert every element into the
#     # already sorted left portion of the array.
#     for pass_num in range(1, length):

#         # Store the current element.
#         # This value will be inserted into
#         # its correct position.
#         key = arr[pass_num]

#         # Start comparing from the element
#         # immediately before the key.
#         j = pass_num - 1

#         # Shift all elements greater than the key
#         # one position to the right.
#         #
#         # Why shift?
#         # Because we want to create an empty spot
#         # where the key can be inserted.
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1

#         # Insert the key into the first position
#         # where every element on the left
#         # is smaller than or equal to it.
#         arr[j + 1] = key

#     # Return the sorted array.
#     return arr


# print(insertion_sort([2, 5, 6, 1, 3, 4]))


# | Bubble Sort                                     | Insertion Sort                                            |
# | ----------------------------------------------- | --------------------------------------------------------- |
# | Compares adjacent elements                      | Compares the current element with the sorted left portion |
# | Swaps elements                                  | Shifts elements and inserts the key                       |
# | Largest element reaches the end after each pass | Sorted portion grows from left to right                   |
# | Best case: O(n) with optimization               | Best case: O(n) naturally                                 |
# | Stable                                          | Stable                                                    |
# | In-place                                        | In-place                                                  |
