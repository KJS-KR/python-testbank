# 1436번, 영화감독 숌

N = int(input())


num = 666
count = 0
while(1):
    if '666' in str(num):
        count += 1
        if count == N:
            print(num)
            break
        
    num += 1