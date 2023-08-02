# 2164번, 카드2

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque([])

for i in range(n):
    queue.append(i+1)
    
while(True):
    if len(queue) == 1:
        print(queue[0])
        break
    
    queue.popleft()
    x = queue.popleft()
    queue.append(x)