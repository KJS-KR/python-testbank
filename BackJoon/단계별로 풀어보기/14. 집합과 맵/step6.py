# 1764, 듣보잡

N, M = map(int, input().split())

dic = {}
for i in range(N+M):
    name = input()
    
    if name not in dic:
        dic[name] = 1
    else:
        dic[name] += 1

count = 0
dup = []
for i in dic:
    if dic[i] == 2:
        dup.append(i)
        count += 1

print(count)
for i in sorted(dup):
    print(i)