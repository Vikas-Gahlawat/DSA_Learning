def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    for n in range(len(arr) - 1):
        swapped = False
        for i in range(len(arr) - 1 - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr
            
bubble_sort([2, 5, 6, 1, 3, 4])



# def bubble_sort(arr):
#     """
#     Sorts a list in ascending order using the Bubble Sort algorithm.

#     Time Complexity:
#         Best Case : O(n)      -> Already sorted (because of swapped optimization)
#         Average   : O(n²)
#         Worst     : O(n²)

#     Space Complexity:
#         O(1) -> Sorting happens in-place.

#     Bubble Sort is a stable sorting algorithm.
#     """

#     # Store the length once instead of calling len(arr) repeatedly.
#     length = len(arr)

#     # If the list has 0 or 1 element, it is already sorted.
#     if length <= 1:
#         return arr

#     # Outer loop controls how many passes we make.
#     # After every pass, the largest unsorted element moves
#     # ("bubbles") to its correct position at the end.
#     for pass_num in range(length - 1):

#         # This flag checks whether any swap happened during the pass.
#         # If no swaps occur, the array is already sorted,
#         # so we can stop early.
#         swapped = False

#         # Inner loop compares adjacent elements.
#         #
#         # Notice:
#         # length - 1 - pass_num
#         #
#         # Why?
#         # Because after every pass, the largest element
#         # is already in its correct position at the end.
#         # No need to compare it again.
#         for i in range(length - 1 - pass_num):

#             # If left element is larger than the right,
#             # swap them.
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swapped = True

#         # If no swaps happened in this entire pass,
#         # the list is already sorted.
#         if not swapped:
#             break

#     # Return the sorted list.
#     return arr


# print(bubble_sort([2, 5, 6, 1, 3, 4]))