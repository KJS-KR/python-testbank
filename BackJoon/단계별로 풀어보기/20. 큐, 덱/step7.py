# 24511번, queuestack

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
seq_A = list(map(int, input().split())) # 1 == queue, 0 == stack
seq_B = list(map(int, input().split())) # i번 자료구조에 초기값

m = int(input())
seq_C = list(map(int, input().split())) # 삽입할 수열 길이

# 스택은 무시, 큐만 deque에 추가
queue = deque([])

for i in range(n):
    if seq_A[i] == 0:
        queue.appendleft(seq_B[i])
    else:
        if queue == []:
            print(*seq_C)
            sys.exit()
            
# deque가 하나의 큐처럼 작동
for i in range(m):
    queue.append(seq_C[i])
    print(queue.popleft(), end=" ")