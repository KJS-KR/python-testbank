# 5073번, 삼각형과 세 변

while(1):
    counter = {}
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    list_t = [x, y, z]

    for i in list_t:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    if max(list_t) >= (sum(list_t) - max(list_t)):
        print("Invalid")
    elif 3 in counter.values():
        print("Equilateral")
    elif 2 in counter.values():
        print("Isosceles")
    else:
        print("Scalene")