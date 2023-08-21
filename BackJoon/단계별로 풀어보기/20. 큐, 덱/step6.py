# 2346번, 풍선 터뜨리기

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        # rotate 파라미터가 음수, 제일 앞이 제일 뒤으로
        q.rotate(-(paper - 1))
    elif paper < 0:
        # rotate 파라미터가 양수, 제일 뒤가 제일 앞으로
        q.rotate(-paper)
    
print(' '.join(map(str, ans)))