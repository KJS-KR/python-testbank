def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 예시로 정렬할 배열
arr = [7, 2, 1, 6, 8, 5, 3, 4]

# 퀵 정렬 수행
sorted_arr = quicksort(arr)

# 결과 출력
print(sorted_arr)