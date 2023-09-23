# 2447번, 별 찍기 - 10

import sys
input = sys.stdin.readline

def star_taking(n):
    middle_point = int(n / 3)
    if middle_point == 1:
        pass
    else:
        star_taking(middle_point)
        
    middle_point_list = [n for n in range(middle_point, middle_point*2)]
    for i in range(n):
        if i > 0:
            print()
        for j in range(n):
            if i in middle_point_list and j in middle_point_list:
                print(' ', end='')
            else:
                print("*", end='')
            
if '__main__':
    n = int(input())
    star_taking(n)