# 10816번, 숫자 카드 2

import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

dic = {}

for i in cards:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in check:
    if i not in dic:
        print(0, end=' ')
    else:
        print(dic[i], end=' ')