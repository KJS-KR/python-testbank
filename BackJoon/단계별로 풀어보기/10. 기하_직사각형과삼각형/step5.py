# 9063번, 대지

N = int(input())

point_list = [[],[]]
for i in range(N):
    x, y = map(int, input().split())

    point_list[0].append(x)
    point_list[1].append(y)

x_max = max(point_list[0])
x_min = min(point_list[0])

y_max = max(point_list[1])
y_min = min(point_list[1])

print((x_max - x_min) * (y_max - y_min))