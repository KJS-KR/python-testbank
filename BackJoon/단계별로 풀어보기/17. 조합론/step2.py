# 24724번, 녹색거탑

N = int(input())

x = 1
for i in reversed(range(1, N+1)):
    x = x * i
    
print(x)