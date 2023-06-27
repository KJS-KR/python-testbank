# 2501번, 약수구하기
try:
    N, K = map(int, input().split())

    divisor = []
    for i in range(1, N+1):
        if N % i == 0:
            divisor.append(i)

    print(divisor[K-1])
except:
    print(0)