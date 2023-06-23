# 아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다. 
# 이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 
# 영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다. 
# 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 
# 이런 식으로 다섯 개의 단어를 만든다. 
# 아래 그림 1은 영석이가 칠판에 붙여 만든 단어들의 예이다.

# max_len = 0
# total = []
# for i in range(5):
#     words = list(map(str, input().split()))
#     total.append(words)
#     if len(words) > max_len:
#         max_len = len(words)

# # for i in range(len(total)):
# #     if len(total[i]) < max_len:
# #         for j in range(max_len-len(total[i])):
# #             total[i].append("")
            
# # for row in range(max_len):
# #     for colunm in range(len(total)):
# #         print(total[colunm][row], end="")

# for column in range(5):
#     for row in range(max_len):
#         if 
#         print(total[column][row], end="")

c = [[] for i in range(15)]

for i in range(5):
    words = input()
    # print(words)
    for j in range(len(words)):
        c[j].append(words[j])

for i in c:
    # print(len(i))
    for j in range(len(i)):
        print(i[j], end='')
