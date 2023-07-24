# 2798번, 블랙잭

N, M = map(int, input().split())

c = list(map(int, input().split()))

max = M
target = 0
for i in range(len(c)-2): # 1 2 3 / 4 5
    for j in range(i+1, len(c)-1): # 2 3 4 5
        for k in range(j+1, len(c)):  # 3 4 5
            sum = c[i] + c[j] + c[k]
            if (M - sum) >= 0 and (M - sum) < max:
                # print(c[i], c[j], c[k])
                max = M - sum
                # print(max)
                target = sum
                # print(target)

# print("----------------")
# print(sum)
print(target)


# 500 - 497 == 0 이상
# 500 - 497 == 3 