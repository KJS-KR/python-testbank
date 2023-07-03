# 10815번, 숫자카드
import sys

N = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in range(N):
    dic[li[i]] = 0

for i in range(M):
    if cards[i] not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ')