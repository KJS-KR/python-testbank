hour = int(input())

count = 0
for h in range(hour + 1):
    for minute in range(60):
        for second in range(60):
            time = str(h) + str(minute) + str(second)
            if "3" in time:
                count += 1

print(count)
