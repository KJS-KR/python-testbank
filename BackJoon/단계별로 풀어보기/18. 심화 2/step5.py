# 20920번, 영단어 암기는 괴로워
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

dic = {}
for _ in range(n):
    word = input().rstrip()
    
    if len(word) >= m:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1

word_lst = sorted(dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수

for i in word_lst:
    print(i[0])