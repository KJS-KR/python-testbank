# 24268번, 알고리즘 수업 - 점근적 표기 1

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

f = a1 * n0 + a0

c_x_g = c * n0

if f <= c_x_g and a1 <= c:
    print(1)
else:
    print(0)
