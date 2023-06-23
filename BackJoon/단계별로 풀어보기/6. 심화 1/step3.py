# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())

null_space = " "
star = "*"
# 4 3 2 1 0 1 2 3 4
# 1 2 3 4 5 4 3 2 1


# -4 -3 -2 -1 0 1 2 3 4

# 1 3 5 7 9 7 5 3 1



# -> 5

# 1 2 3 4 5 6 7 8 9
for i in range(1, 2*N):
    
    # 공백 : 4 3 2 1 0 1 2 3 4
    # * : 1 3 5 7 9 7 5 3 1
    print(null_space*abs(i-N) + star*abs(abs(i-N)*2-(2*N-1)))
