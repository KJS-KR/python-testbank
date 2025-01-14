n = int(input())

directions = list(map(str, input().split()))

print(directions)

x, y = 1, 1

for direction in directions:
    if direction == "L":
        if y > 1:
            y -= 1
    elif direction == "R":
        if y < n:
            y += 1
    elif direction == "U":
        if x > 1:
            x -= 1
    elif direction == "D":
        if x < n:
            x += 1

print(x, y)
