# 2581번, 소수

M = int(input())
N = int(input())

list_de = []
for i in range(M, N+1):
    count_de = 0
    if i > 1:
        for j in range(1, i+1):
            # print(j, end=' ')
            if i % j == 0:
                count_de += 1
        if count_de == 2:
            list_de.append(i)
if list_de :
    print(sum(list_de))
    print(min(list_de))
else:
    print(-1)