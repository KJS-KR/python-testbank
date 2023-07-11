# 4134번, 다음 소수
# 임의의 양수 M이 합성수이면 √m 보다 작거나 같은 약수를 가진다.

import sys
input = sys.stdin.readline

T = int(input())

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(x**0.5)+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

for _ in range(T):
    n = int(input())

    while(True):
        if n == 0 or n == 1:
            print(2)
            break
        if is_prime_number(n):
            print(n)
            break
        else:
            n += 1
