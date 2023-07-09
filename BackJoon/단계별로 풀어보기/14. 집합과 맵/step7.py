# 대칭 차집합

A, B = map(int, input().split())

set_A = list(map(int, input().split()))
set_B = list(map(int, input().split()))

dic_A = {}
dic_B = {}

for i in set_A:
    dic_A[i] = 1

for i in set_B:
    dic_B[i] = 1
    
for i in set_A:
    if i in dic_B:
        dic_B[i] -= 1 

for i in set_B:
    if i in dic_A:
        dic_A[i] -= 1 
        
count = 0
for i in dic_A:
    if dic_A[i] == 1:
        count += 1
for i in dic_B:
    if dic_B[i] == 1:
        count += 1
    
print(count)
    

        