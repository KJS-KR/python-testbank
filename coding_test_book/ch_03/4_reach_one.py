# example 1
n, k = map(int, input().split())

cnt = 0
while True:
    if n % k == 0:
        n /= k
    else:
        n -= 1

    cnt += 1

    if n == 1:
        break
print(cnt)

# example 2

result = 0
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1
print(result)
