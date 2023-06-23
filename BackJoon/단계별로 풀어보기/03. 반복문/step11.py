# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

A = 1
B = 1
while(A != 0 and B != 0):
    A, B =  map(int, sys.stdin.readline().split())

    if A == 0 and B == 0:
        break
    
    print(A + B)

