# 10진법 수 N이 주어진다. 
# 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 
# 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# : 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

# N, b = input().split()
# ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# N = N[::-1]
# result = 0

# for i,n in enumerate(N):
#     result += (int(b)**i)*(ary.index(n))
# print(result)

# # 60466175
# # 6*(10**7) 

N, B = map(int, input().split())
s = ' '
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


while(N):
    s += str(arr[N%B])
    N //= B

print(s[::-1])