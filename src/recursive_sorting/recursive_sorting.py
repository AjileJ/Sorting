import math
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a_index = 0
    b_index = 0
    
    for i in range(elements):
        
        if a_index == len(arrA):
            merged_arr[i:] = arrB[b_index:]
            break
        if b_index == len(arrB):
            merged_arr[i:] = arrA[a_index:]
            break
        if arrA[a_index] <= arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index = a_index + 1
        else:
            merged_arr[i] = arrB[b_index]
            b_index = b_index + 1    
    
    return merged_arr











# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # TO-DO
    length = len(arr)
    if length == 1 or length == 0:
      return arr
    breakIndex = math.floor(length/2)
    
    leftArray = arr[:breakIndex]
    rightArray = arr[breakIndex:]
    
    leftArray = merge_sort(leftArray)
    rightArray = merge_sort(rightArray)
    
    return merge(leftArray, rightArray)













# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
