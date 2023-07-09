# 11478번, 서로 다른 부분 문자열의 개수

s = input()
rag = 0
dic = {}
for i in reversed(range(len(s))): # 4 3 2 1 0
    rag += 1
    for j in range(i+1): # 0 1 2 3 4, 0 1 2 3, 0 1 2, 0 1 , 0
        if s[j:j+rag] not in dic:
            dic[s[j:j+rag]] = 1
    
print(len(dic))