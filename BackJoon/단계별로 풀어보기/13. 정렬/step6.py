# 1427번, 소트인사이드

N = input()

li = []
for i in range(len(N)):
    li.append(int(N[i]))

for i in range(len(N)):
    print(str(sorted(li, reverse=True)[i]), end='')