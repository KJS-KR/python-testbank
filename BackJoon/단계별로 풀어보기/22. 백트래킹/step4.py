# 15652번, N과 M (4)
from copy import deepcopy
from time import time

n, m = map(int, input().split())

s = []
visited = [0] * (n + 1)


def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i] == m:
            continue
        visited[i] += 1
        s.append(i)
        dfs()
        s.pop()
        visited[i] -= 1


dfs()
