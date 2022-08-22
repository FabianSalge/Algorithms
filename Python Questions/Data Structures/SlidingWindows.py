from typing import List


def fixed_sliding_window(arr: List[int], k: int) -> List[int]:
    # Sum up first subarray and add it to result
    curr_subarr = sum(arr[:k])
    result = [curr_subarr]

    # To get next subarray, add next value and remove first value
    for i in range(1, len(arr)-k+1):
        curr_subarr = curr_subarr - arr[i-1]
        curr_subarr = curr_subarr + arr[i+k-1]

        result.append(curr_subarr)
    
    return result


# Algorithm for finding the minimum length with sum smaller than x --> O(n)
def dynamic_sliding_window(arr: List[int], x: int) -> int:
    # Track min value
    min_length = float('inf')

    # Current range and sum for sliding window
    start = 0
    end = 0
    current_sum = 0

    # Extend sliding window until criteria is met
    while end < len(arr):
        current_sum += arr[end]
        end += 1

        # Contract sliding window until no longer meets condition
        while start < end and current_sum >= x:
            current_sum -= arr[start]
            start += 1

            # Update min length if shorter than current min
            min_length = min(min_length, end-start+1)


    return min_length

test = [1,20,3,4,5,6,7,8]
print(fixed_sliding_window(test,3))
print(dynamic_sliding_window(test,21))