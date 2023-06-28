# 2839번, 설탕 배달

N = int(input())

count_5 = 0
count_3 = 0

while(N > 0):
    if N % 5 != 0:
        N -= 3
        count_3 += 1   
        # if N % 5 == 0:
        #     N -= 5 * count_5
        #     count_5 = N // 5
        #     break
        # else:
        #     continue
    else:
        count_5 = N //5
        N -= 5 * count_5
        break

if N == 0:
    print(count_3 + count_5)
else:
    print(-1)