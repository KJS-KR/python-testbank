# 11651, 좌표 정렬하기

N = int(input())

li = []
for i in range(N):
    x, y = map(int, input().split())
    li.append([y, x])

for y, x in sorted(li):
    print(x, y)