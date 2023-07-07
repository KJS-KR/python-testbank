# 7785번, 회사에 있는 사람

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N+1):
    a = input().rstrip()

    dic[i] = a
    dic[a] = i

for i in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(dic[int(q)])
    else:
        print(dic[q])