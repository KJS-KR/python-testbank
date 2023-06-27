# 9506번, 약수들의 합

N = 0
while(1):
    N = int(input())
    if N < 0:
        break
    divisor = []
    for i in range(1, N+1):
        if N % i == 0:
            divisor.append(i)
    
    # print(sum(divisor[:-2]))
    # print(divisor[-1])
    if (sum(divisor[:-1]) ==  divisor[-1]):
        print(str(divisor[-1]) + ' = ', end='')
        for j in divisor[0:-2]:
            print(str(j) + ' + ', end='')
        print(divisor[-2])
    else:
        print(f"{divisor[-1]} is NOT perfect.")
