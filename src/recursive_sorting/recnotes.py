# 1. A recursive algorithm must have a base case.
# 2. A recursive algorithm must change its state and move towards the base case.
# 3. A recursive algorithm must call itself, recursively.

# Print every number, starting at 'number', until you reach 0

def recurse(number):
    if number  <= 0:
        return
    else:
        print(number)
        number -= 1
        recurse(number)
        
    

#recurse(5)    


# Fibonacci Sequence [1,1,2,3,5,8,13,21,34]
# Return the Nth Fibonacci Number

def fibonacci(n):
    if n < 0:
        print("Negative numbers are not valid")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Return (n - 1) + (n - 2)                      
        return fibonacci(n - 1) + fibonacci(n - 2)
                          
    
print('fib',fibonacci(4))  


## Quick Sort ##

# [5 9 3 7 2 8 1 6]

# [3 2 1] [5] [9 7 8 6] 
# [2 1] [3] [] [5] [7 8 6] [9] []
# [1] [2] [3] [5] [6] [7] [8] [9] 

# Decide on base case
# -base case is []
# Find the pivot point
# Partition data to the left and right of the pivot
# smaller than pivot <- left [pivot] right -> larger than pivot 
# what if they are the same size as pivot? pick left or right

# repeat, recurse
my_list = [2,6,3,5,7,8,1,9,4]

def partition(data):
    left = []
    pivot = data[0]
    right = []
    
    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return left, pivot, right

def quicksort(data):
    if data == []:
        return data
    
    left, pivot, right = partition(data)
    
    return quicksort(left) + [pivot] + quicksort(right)  

print(quicksort(my_list))          





    
