# example 1
arr = list(map(int, input().split()))

table = []
for i in range(arr[0]):
    num_cards = list(map(int, input().split()))
    table.append(num_cards)

minimums = []
for cards in table:
    minimum = min(cards)
    minimums.append(minimum)

print(max(minimums))

# example 2
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)
    result = max(result, min_value)

print(result)
