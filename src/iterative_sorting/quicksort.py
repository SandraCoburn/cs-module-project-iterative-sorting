#partition fn handles the work of selecting a pivot element and partioning
#the data in the array around pivot
#returns the left partition, the pivot and the right partition

def partition(arr):
    #pick the first element as the pivot element
    pivot = arr[0]
    left = []
    right = []
    #iterate through the rest of the array,putting each elenent in the appropriate bucket
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return left, pivot, right

def quicksort(arr):
    #base case
    #if the length of the array is 0
    if len(arr) <= 1:
        return arr
    #how do we get closer to our base case
    left, pivot, right = partition(arr)
    return quicksort(left) + [pivot] + quicksort(right)

arr = [13,27,5,18,3,19,22,16]
print(quicksort(arr))

def quicksort2(data):
    #check if data has 1 or 0 elements
    #base case, a side only contains a single element
    if len(data) <= 1:
        return data

    #partition the data
    #start by choosing a pivot (choose the first item in the list)
    pivot = data[0]
    #we need to create storage for the LHS and the RHS
    left = []
    right = []

    #We need to loop through each item
    for current in data[1:]:
        #if it's smaller, add to LHS storage
        if current <= pivot:
            left.append(current)
        else:
        #if it's bigger, add to RHS storage
            right.append(current)

    #(recursive case) Recursively quick sort LHS and RHS until
    return quicksort(left) + [pivot] + quicksort(right) #add brackets to pivot to turn it into a lsit

print(quicksort2(arr))
