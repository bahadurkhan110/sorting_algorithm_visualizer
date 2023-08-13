def quicksort(arr, low, high, k):
    if low < high and high - low >= k:
        # partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        # sort the left and right subarrays
        yield arr, low, high, pivot_index, -1

        yield from quicksort(arr, low, pivot_index - 1, k)
        yield from quicksort(arr, pivot_index + 1, high, k)
    else:
        # if the subarray has fewer than k elements, sort it using insertion sort
        yield from insertion_sort(arr, low, high)

def partition(arr, low, high):
    # choose the pivot element
    pivot = arr[high]
    # initialize the pivot index
    pivot_index = low
    # iterate over the subarray
    for i in range(low, high):
        # if the current element is less than or equal to the pivot
        if arr[i] <= pivot:
            # swap the current element with the element at the pivot index
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
            # increment the pivot index
            pivot_index += 1
    # swap the pivot element with the element at the pivot index
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    # return the pivot index
    return pivot_index

def insertion_sort(arr, low, high):
    # iterate over the subarray
    for i in range(low + 1, high + 1):
        # store the current element
        current = arr[i]
        # initialize the position variable
        pos = i
        # iterate over the sorted subarray
        while pos > low and arr[pos - 1] > current:
            yield arr, pos, -1, i, -1
            # move the elements to the right by one position
            arr[pos] = arr[pos - 1]
            pos -= 1
        # insert the current element into the correct position
        arr[pos] = current


def bonus(arr, *args):
    # sort the array using quicksort
    yield from quicksort(arr, 0, len(arr) - 1, 2)



# The value of k in the hybrid_quicksort() function depends on the specific requirements of the application.
# It is a parameter that can be adjusted to find the best trade-off between performance and efficiency for a given array.
# One way to determine the value of k is to experiment with different values and measure the performance of the hybrid_quicksort()
# function on different arrays. For example, you could try sorting the same array with different values of k and measure the time
# it takes for each sorting operation. You could then choose the value of k that results in the fastest sorting time for that array.
# Another way to determine the value of k is to use theoretical analysis to estimate the performance of the hybrid_quicksort()
# function for different values of k. This can be more complex, but it can provide a more accurate prediction of the performance
# of the algorithm for a given array. Ultimately, the choice of k will depend on the specific requirements of the application and
# the characteristics of the array being sorted.