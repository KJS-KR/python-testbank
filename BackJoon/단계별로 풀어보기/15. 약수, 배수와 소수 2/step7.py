# 4948번, 베르트랑 공준
# 임의의 양수 M이 합성수이면 √m 보다 작거나 같은 약수를 가진다.

import sys

all_list = list(range(2, 246912))
memo = []

for i in all_list:
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        # x가 해당 수로 나누어떨어진다면
        if i % j == 0:
            break
    else:   
        memo.append(i)

input = sys.stdin.readline

while(True):
    n = int(input().strip())
    count = 0

    if n == 0:
        break

    for i in memo:
        if n < i <= 2*n:
            count += 1 
    print(count)



