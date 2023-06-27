# 11653번, 소인수분해

N = int(input())
i = 2
while(N != 1):

    if N % i == 0:
        print(i)
        N = N / i
        i = 2
    else:
        i += 1