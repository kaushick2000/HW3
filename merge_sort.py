def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    # Split the array into two halves and store the one half in left_half and the other in right_half
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])


    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0


    while left_index < len(left) and right_index < len(right):
        # Check the left value of particular index is lesser than the right value of that index if so store the left value to the sortedarray
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        # Or else store the right value to the sortedarray
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # If there are remaining elements in left or right, add them
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

array = [5,2,4,7,1,3,2,6]
sorted_array = merge_sort(array)
print("Sorted array:", sorted_array)
