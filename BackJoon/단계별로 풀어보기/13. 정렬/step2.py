# 2587번, 대표값2

n_list = []
for _ in range(5):
    n_list.append(int(input()))

avg = sum(n_list)/5
center = sorted(n_list)[len(n_list)//2]

print(int(avg))
print(center)