# 1018번, 체스판 다시 칠하기

row, col = map(int, input().split())

board = []
count = []

for _ in range(row):
    board.append(input())
    
for i in range(row-7):
    for j in range(col-7):
        start_W = 0
        start_B = 0
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'W':
                        start_W += 1
                    if board[x][y] != 'B':
                        start_B += 1
                else:
                    if board[x][y] != 'B':
                        start_W += 1
                    if board[x][y] != 'W':
                        start_B += 1
        
        count.append(min(start_B, start_W))

print(min(count))
        
        



        