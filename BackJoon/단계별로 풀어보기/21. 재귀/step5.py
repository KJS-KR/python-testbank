# 4779번, 칸토어 집합

import sys
input = sys.stdin.readline

def cantor(n, start, end):
    if n == 0:
        return
    
    # 3등분
    length = (end - start + 1) // 3
    
    # 왼쪽
    cantor(n - 1, start, start + length - 1)
    
    # 가운데 -> 공백으로 바꾸기
    for k in range(start + length, start + length * 2):
        answer[k] = ' '
        
    # 오른쪽
    cantor(n - 1, start + length * 2, start + length * 3 -1)
    
while True:
    try:
        n = int(input())
        if n < 0 or n > 12:
            break
        else:
            answer = ['-'] * (3 ** n)
            cantor(n, 0, 3 ** n - 1)
            print(''.join(answer))
    except:
        break
    