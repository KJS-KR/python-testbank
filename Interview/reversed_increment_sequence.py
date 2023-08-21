def print_sequence(N):
    num = 1
    increasing = True

    for _ in range(N):
        print(num, end=" ")

        if increasing:
            num += 1
            if abs(num) % 10 == 7 or '7' in str(num):
                increasing = False
        else:
            num -= 1
            if '7' in str(num):
                increasing = True

N = int(input("N을 입력하세요: "))
print_sequence(N)