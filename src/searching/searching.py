def linear_search(arr, target):
    # Search the whole array 
    for n in range(len(arr)):
        #search for the target
       
        if arr[n] == target:
            #print(n)
            #return index of target
            
            return n

    return -1   # not found

# arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7, -4]
# print(linear_search(arr, 9))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # iterate the array by creating a low pointer and high pointer(last item in the list)
    low = 0
    high = len(arr) -1
    #create a loop that will continue while low is less than or equel to the hig pointer
    while low <= high:
        #get middle index
        midd_point = (low + high) // 2
        #retrieve the item with that index from list
        guess = arr[midd_point]
        #There are three options, correct, too high or too low
        if guess == target:
            return midd_point
        if guess > target:
            high = midd_point - 1

        else:
            low = midd_point + 1

    return -1  # not found
