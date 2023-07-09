# 7785번, 회사에 있는 사람

import sys

N = int(sys.stdin.readline())
dic = {}

for _ in range(N):
    name, log = map(str, sys.stdin.readline().split())
    if log == 'enter':
        dic[name] = log
    else:
        del dic[name]

dic = sorted(dic.keys(), reverse=True)

for i in dic:
    print(i)