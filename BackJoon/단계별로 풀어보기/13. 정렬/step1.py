# 2750번, 수 정렬하기

N = int(input())

n_list = []
for _ in range(N):
    n = int(input())
    n_list.append(n)

for i in range(N):
    n_min = min(n_list)
    print(n_min)
    n_list.pop(n_list.index(n_min))
