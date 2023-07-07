import sys
input = sys.stdin.readline

N = int(input())
n_list = []

for _ in range(N):
    n = int(input())
    n_list.append(n)

for i in sorted(n_list):
    print(i)