# 2108번, 통계학
import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    li.append(int(input()))
    
li = sorted(li)

mean = round(sum(li)/len(li))
center = li[int(n/2)]

dic_count = {}
for i in li:
    if i not in dic_count:
        dic_count[i] = 1
    else:
        dic_count[i] += 1
        

max_dic_count_li = []
max_value = dic_count[max(dic_count, key=dic_count.get)]
for n, c in enumerate(dic_count):
    if dic_count[c] == max_value:
        max_dic_count_li.append(c)
        max_dic_count_li.append(dic_count[c])
        
if len(max_dic_count_li) > 3:
    max_c = max_dic_count_li[2]
else:
    max_c = max_dic_count_li[0]

rang = len(range(min(li), max(li)))

print(mean)
print(center)
print(max_c)
print(rang)

