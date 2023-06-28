def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]              # 중앙값 찾기
    print("pivot: ", pivot)
    left = [x for x in arr if x < pivot]    # 중앙값보다 작은 것 모두 left로
    print("left: ", left)
    middle = [x for x in arr if x == pivot] # 중앙값 middle
    print("middle: ", middle)
    right = [x for x in arr if x > pivot]   # 중앙값보다 큰 것 모두 right
    print("right: ", right)
    
    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 2, 9, 1, 6, 3]

sorted_arr = quick_sort(arr)

print(sorted_arr)  # Output: [1, 2, 3, 5, 6, 9]
