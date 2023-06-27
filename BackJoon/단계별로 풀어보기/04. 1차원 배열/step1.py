# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

N = int(input())

N_list = list(map(int, input().split()))

v = int(input())

chk = 0
for i in N_list:
    if i == v:
        chk = chk + 1

print(chk)