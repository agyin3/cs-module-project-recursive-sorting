# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a_idx = 0
    b_idx = 0

    for i in range(len(merged_arr)):
        # b_idx is out of range
        if b_idx > len(arrB) - 1:
            # all arrB items have been sorted so 
            # we can sort rest of arrA
            merged_arr[i] = arrA[a_idx]
            a_idx += 1

        # a_dx is out of range
        elif a_idx > len(arrA) - 1:
            # all arrA items have been sorted so 
            # we can sort rest of arrB
            merged_arr[i] = arrB[b_idx]
            b_idx += 1

        # both a_dx and b_idx are in range
        else:
            if arrA[a_idx] < arrB[b_idx]:
                merged_arr[i] = arrA[a_idx]
                a_idx += 1

            else:
                merged_arr[i] = arrB[b_idx]
                b_idx += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    middle = len(arr) // 2
    LHS = arr[:middle]
    RHS = arr[middle:]

    if len(LHS) > 1:
        LHS = merge_sort(LHS)

    if len(RHS) > 1:
        RHS = merge_sort(RHS)

    arr = merge(LHS, RHS)



    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

