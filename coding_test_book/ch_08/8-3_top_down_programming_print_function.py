# 메모이제이션(Memoization) 리스트
d = [0] * 100


# 파보나치 함수 기반(재귀) 탑다운 다이나믹 프로그래밍
def fibo(x):
    print("f(" + str(x) + ")", end=" ")
    # 종료 조건(1 혹은 2 일 때 1을 반환
    if x == 1 or x == 2:
        return 1

    # 이미 계산한적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면 점화식에 따라 파보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))
