# 11050번, 이항 계수 1

N, K= map(int, input().split())

n_fac = 1
for i in reversed(range(1, N+1)):
    n_fac = n_fac * i

k_fac = 1
for i in reversed(range(1, K+1)):
    k_fac = k_fac * i

n_k_fac = 1
for i in reversed(range(1, N-K+1)):
    n_k_fac = n_k_fac * i
    
print(int(n_fac/(k_fac*n_k_fac)))
