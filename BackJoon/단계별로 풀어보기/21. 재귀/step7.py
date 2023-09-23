# 11729번, 하노이 탑 이동 순서

N = int(input())
MSG_FORMAT = "{} {}"

# start = 출발점
# via = 경유점
# to = 도착점

def move(N, start, to):
    print(MSG_FORMAT.format(start, to))
    
def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

total_move = 2**N - 1

print(total_move)
hanoi(N, '1', '3', '2')