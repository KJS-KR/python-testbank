# 스택, 10773번

import sys

input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    comm = int(input())
    
    if comm == 0:
        li.pop()
    else:
        li.append(comm)
    
    # print(li)

if len(li) == 0:
    print(0)
else:
    print(sum(li))
    