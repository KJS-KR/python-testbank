# 1085번, 직사각형에서 탈출

x, y, w, h = map(int, input().split())

# x축 경계선 까지의 최소값
if w-x <= x:
    x_min = w-x
    if h-y <= y:
        y_min = h-y 
    else:
        y_min = y
else:
    x_min = x
    if h-y <= y:
        y_min = h-y 
    else:
        y_min = y

print((x_min if x_min < y_min else y_min))