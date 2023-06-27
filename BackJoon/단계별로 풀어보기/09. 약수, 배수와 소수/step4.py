# 1978번, 소수 찾기

N = int(input())

list_N = list(map(int, input().split()))

count_de = 0
count_num = 0
for i in list_N:
    count_de = 0
    if i > 1:
        for j in range(1, i+1):
            if i % j == 0:
                count_de += 1
        if count_de == 2:
            count_num += 1
print(count_num)      