# 1934번, 최소공배수

T = int(input())

for i in range(T):
    A, B = map(int, input().split())

    if A <= B:
        div = []
        for j in range(1, A+1):
            if A % j == 0:
                div.append(j)

        for j in div:
            check = B * j
            if check % A == 0 and check % B == 0 :
                min_mul = j * B
                break
                
    else:
        div = []
        for j in range(1, B+1):
            if B % j == 0:
                div.append(j)

        for j in div:
            check = A * j
            if check % A == 0 and check % B == 0 :
                min_mul = j * A
                break

    print(min_mul)