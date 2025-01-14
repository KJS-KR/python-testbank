import random

# N, M, K 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

rand_list = [random.randint(0, 10) for _ in range(n)]
sorted_list = []

for i in range(0, len(rand_list) - 1):
    for j in range(i + 1, len(rand_list)):
        if rand_list[i] < rand_list[j]:
            tmp = rand_list[j]
            rand_list[j] = rand_list[i]
            rand_list[i] = tmp

first = rand_list[0]
second = rand_list[1]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(result)
