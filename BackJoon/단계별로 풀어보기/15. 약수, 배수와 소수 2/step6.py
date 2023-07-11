# 1929번, 소수 구하기
# 임의의 양수 M이 합성수이면 √m 보다 작거나 같은 약수를 가진다.

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        # x가 해당 수로 나누어떨어진다면
        if i % j == 0:
            break
    else:
        print(i)


