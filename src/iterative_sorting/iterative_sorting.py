# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range(i, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        # TO-DO: swap
        
        smaller = arr[smallest_index]
        cur = arr[i]
        arr[i] = smaller
        arr[smallest_index] = cur
    return arr




#TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    done = False
    length = len(arr)
    while not done:
        done = True
        for i in range(0,length -1):
            currIndex = arr[i]
            nextIndex = arr[i + 1]
            if currIndex > nextIndex:
                done = False
                arr[i] = nextIndex
                arr[i + 1] = currIndex

    return arr


# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr