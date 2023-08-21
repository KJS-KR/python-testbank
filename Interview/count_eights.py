def count_eight(N):
    count = 0
    for num in range(1, N + 1):
        count += str(num).count('8')
        if '8' in str(num):
            print(num)
    return count

N = int(input("N을 입력하세요: "))
result = count_eight(N)
print("숫자 8은 총", result, "번 나타납니다.")