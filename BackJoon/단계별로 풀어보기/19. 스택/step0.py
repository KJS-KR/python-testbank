# 28278번, 스택2

import sys
input = sys.stdin.readline

n = int(input())

stk = []
for _ in range(n):
    comm = list(map(str, input().split()))
    
    if comm[0] == "1":
        stk.append(comm[1])
    elif comm[0] == "2":
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif comm[0] == "3":
        print(len(stk))
    elif comm[0] == "4":
        if stk:
            print(0)
        else:
            print(1)
    elif comm[0] == "5":
        if stk:
            print(stk[-1])
        else:
            print(-1)