# 17103번, 골드바흐 파티션

import sys

prime = []
check = [0] * 100
check[0] = 1
check[1] = 1

for i in range(2, 100):
    if check[i] == 0:
        print(i)
        prime.append(i)
        for j in range(2*i, 100, i):
            check[j] = 1
            print(j, check[j])

print(check)
print(prime)

T = int(sys.stdin.readline())

for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    for i in prime:
        if i >= N:
            break
        if not check[N - i] and i <= N-i:  # 순서만 다른거 counting 하지 않기 위해
            print(check[N - i])
            count += 1
    print(count)




