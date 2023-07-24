# 25192번, 인사성 밝은 곰곰이

n = int(input())

log = []
for _ in range(n):
    chat = input()
    log.append(chat)

count = 0
for i in log:
    if i == "ENTER":
        dic = {}
        continue
    if i not in dic:
        dic[i] = 1
        count += 1
    
print(count)