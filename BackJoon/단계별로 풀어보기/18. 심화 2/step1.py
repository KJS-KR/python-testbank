# 1037번, 약수

n = int(input())

div = sorted(list(map(int, input().split())))

print(div[0] * div[-1])