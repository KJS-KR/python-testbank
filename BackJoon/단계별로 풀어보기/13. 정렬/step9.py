# 1181번, 단어 정렬

n = int(input())

word = []
for _ in range(n):
    word.append(input())

set_word = list(set(word))

len_word = []
for i in set_word:
    len_word.append((len(i), i))

sorted_word = sorted(len_word)

for len_word, word in sorted_word:
    print(word)
