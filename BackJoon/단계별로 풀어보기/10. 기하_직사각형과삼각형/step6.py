# 10101번, 삼각형 외우기

list_angle = []
counter = {}
total = 0
for _ in range(3):
    angle = int(input())
    total += angle
    if angle in counter:
        counter[angle] += 1
    else:
        counter[angle] = 1

if total != 180:
    print("Error")
elif 2 in counter.values():
    print("Isosceles")
elif 1 in counter.values():
    print("Scalene")
else:
    print("Equilateral")