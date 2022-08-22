# Divide and conquer similar to binary search. 
# Calculates the probable position of the element we are searching for using: index = low + [(taget-arr[low])*(high-low) / (arr[high]-arr[low])]

def InterpolationSearch(arr, target):
    low = 0
    high = len(arr) - 1

    while (low < high) and (target >= arr[low]) and (target <= arr[high]):
        index = low + int(((float(high - low) / ( arr[high] - arr[low])) * ( target - arr[low])))

        if arr[index] == target:
            return index
        if arr[index] < target:
            low = index + 1
        else:
            high = index + 1
    
    return -1


# The time complexity of interpolation search is O(log log n) when values are uniformly distributed. If values are not uniformly distributed, the worst-case time complexity is O(n), the same as linear search.

# Interpolation search works best on uniformly distributed, sorted arrays. Whereas binary search starts in the middle and always divides into two, interpolation search calculates the likely position of the element and checks the index, making it more likely to find the element in a smaller number of iterations.



