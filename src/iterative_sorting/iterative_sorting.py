# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for unsorted_index in range(cur_index +1, len(arr)):
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Compare the first and second item of a collection
    for item in range(0, len(arr) -1):
    #if the first one is bigger than second, swap items moving lower to left
        for i in range(len(arr)-item-1):
            if  arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    #move to the next item. compare the second item to the third item. if second is bigger, swap the items moving bigger to right
    #Do this for every item until the end of the list
    #repeat setps 1-3(decrementing the end of the list by 1 each time)

    return arr
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(arr1))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # the output array that will haver sorted arr. only integers
    
    if len(arr) > 0:
        maximum = max(arr) + 1
        bucket = [0] * maximum
    else:
        return arr

    #check that array has no negative numbers
    for item in arr:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            #count occurences
            bucket[item] += 1
        
    num_items_before = 0
    #overwrite bucket to hold the next index
    for i, count in enumerate(bucket):
        bucket[i] = num_items_before
        num_items_before += count

    #output list to be filled in
    sorted_list = [None] * len(arr)

    #run through the input list
    for item in arr:
        #place the item in the sorted list
        sorted_list[bucket[item]] = item

        #make sure the next item we see with the same value goes after the one we just place
        bucket[item] += 1

    return sorted_list
