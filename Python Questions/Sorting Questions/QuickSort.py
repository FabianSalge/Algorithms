def partition(arr, low, high):

    # Chose right most pivot
    pivot = arr[high]

    # pointer for greater elements
    i = low - 1

    # loop over all components and compare to pivot point
    for j in range(low, high):
        if arr[j] <= pivot:
            # If element is < pivot swap it with the greater element pointed by i
            i = i + 1
            
            # swap element at ith index with jth
            (arr[i], arr[j]) = (arr[j] , arr[i]) 

    #swap the pivot element with the greater element specified by i
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1

def QuickSort(arr, low, high):

    if low < high:

        pi = partition(arr, low, high)

        # Sort left of pivot 
        QuickSort(arr, low, pi - 1)
        # Sort to right of pivot
        QuickSort(arr, pi + 1, high)