#B진법 수 N이 주어진다. 
# 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
#10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 
# 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

N, B = map(str, input().split())
N = N[::-1]
print(ord(N[0]))


# B진법 -> 10진법
decimal_number = 0

for i in range(len(N)):
    if N[i].isdecimal() is not True:
        decimal_number += (ord(N[i]) - 55)*(int(B)**i)
    else:
        decimal_number += int(N[i])*(int(B)**i)
        
print(decimal_number)

# ----------------------------------------------------------

N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(b)**i)*(ary.index(n))
print(result)