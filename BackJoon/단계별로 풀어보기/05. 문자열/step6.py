# `알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

S = input()

alpha = []
for i in range(ord('a'), ord('z')+1):
    alpha.append(chr(i))

for s in S:
    if s in alpha:
        alpha[alpha.index(s)] = S.index(s)

for i in alpha:
    if type(i) == str:
        alpha[alpha.index(i)] = -1
            
for i in alpha:
    print(i, end=' ')
