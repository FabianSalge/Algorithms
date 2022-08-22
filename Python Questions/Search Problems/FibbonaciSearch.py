# Divide and conquer algorithm similar to binary and jump search 
# Fibbonaci Seq: 0,1,1,2,3,5,8,13,21 ... each elem is addition of previous two 

# Generates the closest fibbonici number greater than or equal to the length of the array
# assigns previous 2 fibbonaci numbers to variables


def FibbonaciSearch(arr, target):
    
    # Last two elements in sequence 
    fibM_previous_2 = 0
    fibM_previous_1 = 1

    fibM = fibM_previous_1 + fibM_previous_2

    while(fibM < len(arr)):
        fibM_previous_2 = fibM_previous_1
        fibM_previous_1 = fibM
        fibM = fibM_previous_1 + fibM_previous_2
    index = -1

    while(fibM > 1):
        i = min(index + fibM_previous_2, (len(arr) - 1))
        if(arr[i] < target):
            fibM = fibM_previous_1
            fibM_previous_1 = fibM_previous_2
            fibM_previous_2 = fibM - fibM_previous_1
            index = i
        elif (arr[i] > target):
            fibM = fibM_previous_2
            fibM_previous_1 = fibM_previous_1 - fibM_previous_2
            fibM_previous_2 = fibM - fibM_previous_1
        else:
            return i
    if (fibM_previous_1 and index < (len(arr)-1) and arr[index+1] == target):
        return index + 1
    
    return -1


# Time complexity: O(logn) - same as binary search
# Used when very large number of elements to search through - without devision opeartor 
