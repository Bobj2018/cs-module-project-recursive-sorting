# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if end >= start:
        # Find the middle of the array
        middle = (start + end) // 2

        # Check if the target equals the middle index
        if target == arr[middle]:
            return middle

        # if not, check if the middle value is greater or less than the target
        if target > arr[middle]:
            return binary_search(arr, target, middle + 1, end)

        if target < arr[middle]:
            return binary_search(arr, target, start, middle - 1)

    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    pass
