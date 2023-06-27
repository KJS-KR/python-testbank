# 5086번, 배수와 약수


while(True):
    A, B = map(int, input().split())

    # if A가 B의 약수, B % A == 0

    # elif A가 B의 배수, A % B == 0

    # else 아무것도 아님

    if A == 0 and B == 0:
        break

    if B % A == 0:
        print("factor")
    elif A % B ==0:
        print("multiple")
    else:
        print("neither")