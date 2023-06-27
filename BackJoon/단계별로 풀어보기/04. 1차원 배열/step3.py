# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

A_list = []
for i in range(9):
    A = int(input())
    A_list.append(A)

max = 0

for i, v in enumerate(A_list):
    if v > max:
        max = v
        idx = i+1

print(max)
print(idx)