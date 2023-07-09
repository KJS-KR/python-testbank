# 1735번, 분수합

# 1. 분모의 해당하는 값들의 최소 공배수를 구한다.
# 2. 최소 공배수 값만큼 분모와 분자에 곱한 후 더하여 결과를 출력

A, B = map(int, input().split())
A_, B_ = map(int, input().split())

A = A * B_ + A_ * B
B = B * B_

mod = A % B

while mod > 0:
    x = B
    y = mod
    mod = x % y

    print(x, y, mod)

print(A//y, B//y)
