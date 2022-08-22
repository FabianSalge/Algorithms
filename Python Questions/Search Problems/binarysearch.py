# Recursive approach
def binarysearch(arr, lo, hi, t):
    
    if hi >= lo:
        # Set pivot
        mid = (hi + lo) / 2

        # Check if target is pivot
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            # Search left of pivot
            return binarysearch(arr, lo, mid - 1, t)
        else:
            # Search right of pivot
            return binarysearch(arr, mid + 1, t)
        
    else: 
        # Item not in array
        return -1

# Non Recursive approach
def binarysearch2(arr, target):
    first = 0
    last = len(arr) -1
    index = -1
    while(first <= last) and (index == -1):
        mid = (first+last) // 2
        if arr[mid] == target:
            index = mid
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return index


# O(logn) time complexity 