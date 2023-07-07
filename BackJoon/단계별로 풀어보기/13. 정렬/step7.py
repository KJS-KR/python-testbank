# 11650, 좌표 정렬하기

N = int(input())

li = []
for i in range(N):
    x, y = map(int, input().split())
    li.append([x, y])

for x, y in sorted(li):
    print(x, y)