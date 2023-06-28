# 18870번, 좌표 압축

N = int(input())
points = list(map(int, input().split()))

dub_points = sorted(list(set(points)))

dic = {dub_points[i] : i for i in range(len(dub_points))}

# print(dic)
for i in points:
    print(dic[i], end=' ')