def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursive call to sort the sub-arrays
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Merge the sorted sub-arrays
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Merge the two sub-arrays in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append the remaining elements, if any
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

arr = [5, 2, 9, 1, 6, 3]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 5, 6, 9]