# 2231번, 분해합

N = int(input())
DS = 0
for i in range(N):
    division_sum = i
    position_sum = 0
    for j in range(len(str(i))):
        position_sum += int(str(i)[j])
    division_sum += position_sum
    
    if division_sum == N:
        DS = division_sum - position_sum
        break

if DS:
    print(DS)
else:
    print(0)
    