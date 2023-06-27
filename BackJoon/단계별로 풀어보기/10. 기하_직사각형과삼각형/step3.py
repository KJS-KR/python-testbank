# 3009번, 네 번째 점

x_list = []
y_list = []
for i in range(3):
    x, y = map(int, input().split())

    x_list.append(x)
    y_list.append(y)

x_max = sum(x_list)
y_max = sum(y_list)

x_dup = [i for i in x_list if x_list.count(i) > 1]
y_dup = [i for i in y_list if y_list.count(i) > 1]

# print(x_dup, y_dup)

print(x_max - x_dup[0]*2, y_max - y_dup[0]*2)