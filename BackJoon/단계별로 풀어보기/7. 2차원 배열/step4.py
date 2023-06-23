# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 
# 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 
# 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

rec = [[0 for _ in range(101)] for _ in range(101)]

num = int(input())
for _ in range(num):
    x, y = list(map(int, input().split()))
    
    for row in range(x, x+10):
        for column in range(y, y+10):
            rec[row][column] = 1
            
result = 0

for i in rec:
    result += i.count(1)
    
print(result)