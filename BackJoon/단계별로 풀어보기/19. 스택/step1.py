# 스택, 10828번

import sys

input = sys.stdin.readline

n = int(input().strip())

result = []

def push(li, num):
    li.append(num)
    return li

def top(li):
    if len(li) == 0:
        print(-1)
    else:
        print(li[-1])
    
def size(li):
    print(len(li))

def pop(li):
    if len(li) == 0:
        print(-1)
    else:
        print(li.pop())

def empty(li):
    if len(li) == 0:
        print(1)
    else:
        print(0)
        
for _ in range(n):
    comm = list(map(str, input().split()))
    
    if comm[0] == "push":
        eval(comm[0] + "(result, comm[1])")
    else:
        eval(comm[0] + "(result)")