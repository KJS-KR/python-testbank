# 15650번, N과 M (2)
from copy import deepcopy

n, m = map(int, input().split())

visited = [False] * (n + 1)
s = []
total = []

def dfs():
    if len(s) == m:
        # print(s)
        total.append(deepcopy(s))
        # print(' '.join(map(str, s)))
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

dfs()

duplicated_list = []
for item in total:
    item = set(item)
    if item not in duplicated_list:
        duplicated_list.append(item)

for item in duplicated_list:
    print(" ".join(map(str, sorted(item))))
