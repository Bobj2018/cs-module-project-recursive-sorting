# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    left, right = 0,0

    for i in range(elements):
        if left == len(arrA):
            merged_arr[i] = arrB[right]
            right += 1
        elif right == len(arrB):
            merged_arr[i] = arrA[left]
            left += 1
        elif arrA[left] <= arrB[right]:
            merged_arr[i] = arrA[left]
            left += 1
        else:
            merged_arr[i] = arrB[right]
            right += 1

    # else, if left is greater, insert right
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    #base case = length of 1
    if len(arr) <= 1 :
        return arr
    else:
        #if not b       ase case, call merge_sort on left and right side of the array
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        # merge arrays
        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
