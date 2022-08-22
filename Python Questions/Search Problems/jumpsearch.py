import math

def jumpsearch(arr, target):
    length = len(arr)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < right and arr[left] <= target:
        right = min(length - 1, left + jump)
        if arr[left] <= target and arr[right] >= target:
            break
        left += jump
    if left >= length or arr[left] > target:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and arr[right] <= target:
        if arr[i] == target:
            return i
        i += 1
    return -1

# This algorithm has O(sqrt(n)). It can be faster than binary search with large numbers
# because it does not use the / operator, which on some systems can be more CPU intensive.
# This search eliminates the / opeartor and can therefore be faster than binary search.