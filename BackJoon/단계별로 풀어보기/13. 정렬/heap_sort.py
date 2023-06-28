def heap_sort(arr):
    n = len(arr)
    
    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap the maximum element with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

def heapify(arr, n, root):
    largest = root  # Assume the root as the largest element
    left = 2 * root + 1
    right = 2 * root + 2
    
    # Check if the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if the right child exists and is greater than the largest
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If the largest element is not the root, swap them
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify(arr, n, largest)
    
arr = [5, 2, 9, 1, 6, 3]
heap_sort(arr)
print(arr)  # Output: [1, 2, 3, 5, 6, 9]