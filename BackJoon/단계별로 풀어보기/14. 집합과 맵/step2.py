# 14425번, 문자열 집합

import sys

N, M = map(int, (sys.stdin.readline().split()))

S = []
for _ in range(N):
    S.append(input())

count_c = 0
for _ in range(M):
    check = input()

    if check in S:
        count_c += 1

print(count_c)