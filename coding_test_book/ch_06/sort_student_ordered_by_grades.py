array = [("A", 85), ("B", 70), ("C", 65), ("D", 99), ("E", 35)]

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=" ")
