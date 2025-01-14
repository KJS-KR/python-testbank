num = 4
length = 6

len_rices = [19, 15, 10, 17]

start = 0
end = max(len_rices)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for len_rice in len_rices:
        if len_rice > mid:
            total += len_rice - mid
    if total < length:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
