# 10814번, 나이순 정렬

n = int(input())

reg_li = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    reg_li.append((age, name))

reg_li.sort(key= lambda x: x[0])

for i in reg_li:
    print(i[0], i[1])