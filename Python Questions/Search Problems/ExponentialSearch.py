from binarysearch import binarysearch2

def ExponentialSearch(arr, target):
    if arr[0] == target:
        return 0
    index = -1
    while index < len(arr) and arr[index] <= target:
        index = index * 2
    return binarysearch2(arr[:min(index, len(arr))], target)

# Exponential search runs in O(log i) time, where i is the index of the item we are searching for. In its worst case, the time complexity is O(log n), when the last item is the item we are searching for (n being the length of the array).

# Exponential search works better than binary search when the element we are searching for is closer to the beginning of the array. In practice, we use exponential search because it is one of the most efficient search algorithms for unbounded or infinite arrays.