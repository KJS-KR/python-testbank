# 28279번, 덱 2

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

deck_ = deque([])
for _ in range(n):
    comm = list(map(str, input().split()))
    
    if comm[0] == "1":
        deck_.appendleft(comm[1])
    elif comm[0] == "2":
        deck_.append(comm[1])
    elif comm[0] == "3":
        if deck_:
            print(deck_.popleft())
        else:
            print(-1)
    elif comm[0] == "4":
        if deck_:
            print(deck_.pop())
        else:
            print(-1)
    elif comm[0] == "5":
        print(len(deck_))
    elif comm[0] == "6":
        if deck_:
            print(0)
        else:
            print(1)
    elif comm[0] == "7":
        if deck_:
            print(deck_[0])
        else:
            print(-1)
    elif comm[0] == "8":
        if deck_:
            print(deck_[-1])
        else:
            print(-1)