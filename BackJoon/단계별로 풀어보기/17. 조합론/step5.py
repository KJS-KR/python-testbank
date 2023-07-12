# 1010번, 다리 놓기

T = int(input())


for _ in range(T):
    N, M = map(int, input().split())
    
    cases = 0
    if N == M:
        print(1)
        
    else:
        n_fac = 1
        for i in reversed(range(1, M+1)):
            n_fac = n_fac * i

        k_fac = 1
        for i in reversed(range(1, N+1)):
            k_fac = k_fac * i

        n_k_fac = 1
        for i in reversed(range(1, M-N+1)):
            n_k_fac = n_k_fac * i
            
        print(int(n_fac/(k_fac*n_k_fac)))  
    